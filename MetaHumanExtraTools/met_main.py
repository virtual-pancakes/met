# Copyright Virtual Pancakes, 2025. All Rights Reserved.
import sys
import os
import importlib
import shutil # type: ignore
import time
import math
import random # type: ignore
import json

import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as om2a
import maya.mel as mel

from dna import BinaryStreamReader, BinaryStreamWriter, AccessMode_Read, AccessMode_Write, OpenMode_Binary, DataLayer_All, FileStream, Status
from dnacalib2 import CommandSequence, DNACalibDNAReader, SetNeutralJointRotationsCommand, SetNeutralJointTranslationsCommand, SetVertexPositionsCommand, SetLODsCommand, CalculateMeshLowerLODsCommand, VectorOperation_Add, RotateCommand
from mh_assemble_lib.control.form import MeshForm, ProcessForm
from mh_assemble_lib.impl.maya.handler import MayaHandler
from mh_assemble_lib.impl.maya.properties import MayaSceneOrient
from mh_assemble_lib.model.dnalib import DNAReader, Layer, DNA
from mh_assemble_lib.impl.maya.scene.mesh_handler import MayaMeshHandler
from mh_assemble_lib.impl.maya.scene.joint_handler import MayaJointHandler
from mh_assemble_lib.impl.maya.scene.sw_handler import MayaSkinWeightsHandler
from mh_assemble_lib.impl.maya.scene.rig_handler import MayaRigHandler
from mh_assemble_lib.impl.maya.properties import MayaConfig
from mh_assemble_lib.model.element import MeshElement

sys.modules["PySide2"] = __import__("PySide6")
sys.modules["PySide2.QtCore"] = sys.modules["PySide6.QtCore"]
sys.modules["PySide2.QtGui"] = sys.modules["PySide6.QtGui"]
sys.modules["PySide2.QtWidgets"] = sys.modules["PySide6.QtWidgets"]

try: importlib.reload(resources.data)
except: import resources.data


def snap_vertices(floating, static, reference_vertex_ids):
    #print("Snapping vertices...")
    #print(f"static: {static}")
    #print(f"floating: {floating}")
    #print(f"reference_vertex_ids: {reference_vertex_ids}")
    floating_path = om2.MSelectionList().add(floating).getDagPath(0)
    static_path = om2.MSelectionList().add(static).getDagPath(0)
    floating_iterator = om2.MItMeshVertex(floating_path)
    static_iterator = om2.MItMeshVertex(static_path)

    while not floating_iterator.isDone():
        static_vertex_id = reference_vertex_ids[floating_iterator.index()]
        static_iterator.setIndex(static_vertex_id)
        floating_iterator.setPosition(static_iterator.position())
        
        floating_iterator.next()

class MetahumanToObj:
    def __init__(self, input_metahuman_folder, input_make_symmetric):
        self.input_metahuman_folder = input_metahuman_folder
        self.input_make_symmetric = input_make_symmetric
        self.head_dna_path = f"{self.input_metahuman_folder}/head.dna"
        self.body_dna_path = f"{self.input_metahuman_folder}/body.dna"

        """
        # Run
        original_warning_state = cmds.scriptEditorInfo(query=True, suppressWarnings=True)
        cmds.scriptEditorInfo(suppressWarnings=True)

        self.run()

        cmds.scriptEditorInfo(suppressWarnings=original_warning_state)
        """
        
    def symmetrize(self, name):
        dagpath = om2.MSelectionList().add(name).getDagPath(0)
        fn_mesh = om2.MFnMesh(dagpath)
        positions = fn_mesh.getPoints()
        mirror_vertex_ids = resources.data.mirror_vertex_ids[name]
        iterator = om2.MItMeshVertex(dagpath)
        
        while not iterator.isDone():
            index = iterator.index()
            mirror_index = mirror_vertex_ids[index]
            position = positions[index]
            mirror_position = positions[mirror_index]
            projected_mirror_position = om2.MPoint(mirror_position)
            projected_mirror_position.x *= -1
            midpoint_vector = (projected_mirror_position - position) / 2
            target_position = position + midpoint_vector
            iterator.setPosition(target_position)

            iterator.next()
    
    def symmetrize_eyelashes(self):
        # Set drivers
        cmds.namespace(add=":driver")
        cmds.namespace(set=":driver")
        drivers_file = os.path.dirname(__file__) + "/resources/drivers.fbx"
        cmds.file(drivers_file, i=True, f=True)
        cmds.namespace(add=":driver_target")
        cmds.namespace(set=":driver_target")
        driver = "driver:cartilage"
        reference_vertex_ids = resources.data.cartilage_reference_vertex_ids
        target = cmds.duplicate(driver)[0]
            
        snap_vertices(driver, "combined", reference_vertex_ids)
        snap_vertices(target, "combined", reference_vertex_ids)  
        bs = cmds.blendShape(target, driver)[0]
        cmds.setAttr(f"{bs}.{om2.MNamespace.stripNamespaceFromName(target)}", 1)

        pw = cmds.proximityWrap("eyelashes")[0]
        cmds.proximityWrap(pw, edit=True, addDrivers="driver:cartilage")
        cmds.setAttr(f"{pw}.wrapMode", 0)
        cmds.setAttr(f"{pw}.smoothInfluences", 1)

        cmds.select("eyelashes")
        cmds.DeleteHistory()
        cmds.namespace(set=":")
    
    def debug(self):
        cmds.file("F:/WorkspaceDesktop/met_tests/temp.mb", o=True, f=True)
        self.symmetrize("combined")
    
    def get_closest_vertex_id_to_point(self, point, mesh, face_iterator):
        # Get closest face
        closest_point_position, closest_face_id = mesh.getClosestPoint(point, om2.MSpace.kWorld)
        
        # Get closest face vertex ids and positions
        face_iterator.setIndex(closest_face_id)
        closest_face_vertex_ids = face_iterator.getVertices()
        closest_face_vertex_positions = face_iterator.getPoints(om2.MSpace.kWorld)
        
        # Get closest face vertex distances to position
        closest_face_vertex_distances_to_position = []
        for face_vertex_position in closest_face_vertex_positions:
            closest_face_vertex_distances_to_position.append(face_vertex_position.distanceTo(point))        
        
        # Get closest vertex id, position and distance to position
        closest_vertex_distance = closest_face_vertex_distances_to_position[0]
        closest_vertex_id = closest_face_vertex_ids[0]
        closest_vertex_position = closest_face_vertex_positions[0]
        for i, distance in enumerate(closest_face_vertex_distances_to_position):
            if distance < closest_vertex_distance: 
                closest_vertex_distance = distance
                closest_vertex_id = closest_face_vertex_ids[i]
                closest_vertex_position = closest_face_vertex_positions[i]

        return closest_vertex_id
    
    def run(self):    
        # start new scene
        original_warning_state = cmds.scriptEditorInfo(query=True, suppressWarnings=True)
        cmds.scriptEditorInfo(suppressWarnings=True)
        cmds.file(new=True, force=True)
        cmds.upAxis(ax="y", rv=True)
        
        # Load LOD0 meshes for each DNA, excluding secomdary meshes
        skip_names = ["saliva", "eyeshell", "eyeEdge", "cartilage"]
        dna_meshes = []
        for dna_path in [self.head_dna_path, self.body_dna_path]:
            print(f"Processing DNA: {dna_path}")        
            input_stream = FileStream(dna_path, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
            reader = BinaryStreamReader(input_stream, DataLayer_All)
            reader.read()
            dna_object = DNA(dna_path, reader)
            form = ProcessForm()
            maya_config = MayaConfig()
            maya_mesh_handler = MayaMeshHandler(dna_object, form, maya_config)
            mesh_element = dna_object.get_mesh(0)
            mesh_elements = dna_object.get_meshes()
            for element in mesh_elements:
                if element.lod == 0 and not any(name in element.name for name in skip_names):
                    #print(f"name: {element.name}, lod: {element.lod}, poly_faces: {element.poly_faces}, poly_connections: {element.poly_connections}")
                    maya_mesh_handler.add_mesh_to_scene(element)
                    maya_mesh_handler.add_mesh_uv(element)
                    maya_mesh_handler.add_mesh_shader(element)
                    dna_meshes.append(element.name)

        # Rename meshes
        combined_meshes = []
        for i, mesh in enumerate(dna_meshes):
            new_name = mesh.replace("_lod0_mesh", "")
            cmds.rename(mesh, new_name)
            combined_meshes.append(new_name)            
                
        # Combine eyes
        cmds.polyUnite("eyeLeft", "eyeRight", name="eyes", mergeUVSets=True, ch=False)
        combined_meshes.pop(combined_meshes.index("eyeLeft"))
        combined_meshes.pop(combined_meshes.index("eyeRight"))
        combined_meshes.insert(0, "eyes")
        
        # Import meshes with polygroups
        cmds.namespace(add=":pgs")
        cmds.namespace(set=":pgs")
        file = os.path.dirname(__file__) + "/resources/meshes_with_pgs.fbx"
        cmds.file(file, i=True)        
        cmds.namespace(set=":")
        
        # Combine head and body meshes
        #cmds.duplicate("head", name="head_lod0_mesh")
        cmds.select("head", "body")
        combined_mesh = cmds.polyUnite(name="combined", ch=False)[0]
        destination_vertex1_position = cmds.xform(f"{combined_mesh}.vtx[27037]", q=True, t=True, ws=True)
        destination_vertex2_position = cmds.xform(f"{combined_mesh}.vtx[45884]", q=True, t=True, ws=True)
        destination_vertex3_position = cmds.xform(f"{combined_mesh}.vtx[49936]", q=True, t=True, ws=True)
        cmds.polyMergeVertex(['combined.vtx[2805:2824]', 'combined.vtx[2873]', 'combined.vtx[2876]', 'combined.vtx[2965]', 'combined.vtx[2997]', 'combined.vtx[5876:5895]', 'combined.vtx[5944]', 'combined.vtx[5947]', 'combined.vtx[11560]', 'combined.vtx[11564]', 'combined.vtx[11567]', 'combined.vtx[11569]', 'combined.vtx[11572]', 'combined.vtx[11575]', 'combined.vtx[11578]', 'combined.vtx[11582]', 'combined.vtx[11585]', 'combined.vtx[11587]', 'combined.vtx[11600]', 'combined.vtx[11795]', 'combined.vtx[11798:11799]', 'combined.vtx[11802:11803]', 'combined.vtx[11805]', 'combined.vtx[11807]', 'combined.vtx[11809]', 'combined.vtx[11811]', 'combined.vtx[11899]', 'combined.vtx[11909:11910]', 'combined.vtx[17607]', 'combined.vtx[17610]', 'combined.vtx[17614]', 'combined.vtx[17617]', 'combined.vtx[17619]', 'combined.vtx[17622]', 'combined.vtx[17626]', 'combined.vtx[17629]', 'combined.vtx[17632]', 'combined.vtx[17635]', 'combined.vtx[17647]', 'combined.vtx[17854]', 'combined.vtx[17856]', 'combined.vtx[17859:17860]', 'combined.vtx[17863]', 'combined.vtx[17865]', 'combined.vtx[17867]', 'combined.vtx[17869]', 'combined.vtx[17871]', 'combined.vtx[17962]', 'combined.vtx[17968]', 'combined.vtx[17972]', 'combined.vtx[24049:24093]', 'combined.vtx[27867]', 'combined.vtx[31694]', 'combined.vtx[33235]', 'combined.vtx[33241]', 'combined.vtx[33244]', 'combined.vtx[33247]', 'combined.vtx[33252]', 'combined.vtx[33255:33256]', 'combined.vtx[33260]', 'combined.vtx[37976]', 'combined.vtx[37980]', 'combined.vtx[38004]', 'combined.vtx[38006:38007]', 'combined.vtx[38009]', 'combined.vtx[38011]', 'combined.vtx[38013]', 'combined.vtx[38015]', 'combined.vtx[38017]', 'combined.vtx[39207]', 'combined.vtx[39219]', 'combined.vtx[39229]', 'combined.vtx[39238]', 'combined.vtx[39276]', 'combined.vtx[40823:40824]', 'combined.vtx[40828]', 'combined.vtx[40833]', 'combined.vtx[40835]', 'combined.vtx[40838]', 'combined.vtx[40843:40844]', 'combined.vtx[45589]', 'combined.vtx[45591]', 'combined.vtx[45613]', 'combined.vtx[45615]', 'combined.vtx[45618]', 'combined.vtx[45620]', 'combined.vtx[45622]', 'combined.vtx[45624]', 'combined.vtx[45626:45627]', 'combined.vtx[46850]', 'combined.vtx[46863]', 'combined.vtx[46873]', 'combined.vtx[46882]'], d=0.01, am=1, ch=0)
        cmds.select(cl=True)
        combined_meshes.pop(combined_meshes.index("head"))
        combined_meshes.pop(combined_meshes.index("body"))
        combined_meshes.insert(0, "combined")
        # Transfer vertex order
        if not cmds.pluginInfo("meshReorder.mll", query=True, loaded=True): cmds.loadPlugin("meshReorder.mll")
        source_vertex1 = "pgs:combined.vtx[26992]"
        source_vertex2 = "pgs:combined.vtx[45796]"
        source_vertex3 = "pgs:combined.vtx[49844]"
        dagpath = om2.MSelectionList().add(combined_mesh).getDagPath(0)
        mesh = om2.MFnMesh(dagpath)
        face_iterator = om2.MItMeshPolygon(dagpath) 
        destination_vertex1_id = self.get_closest_vertex_id_to_point(om2.MPoint(destination_vertex1_position), mesh, face_iterator)
        destination_vertex2_id = self.get_closest_vertex_id_to_point(om2.MPoint(destination_vertex2_position), mesh, face_iterator)
        destination_vertex3_id = self.get_closest_vertex_id_to_point(om2.MPoint(destination_vertex3_position), mesh, face_iterator)
        destination_vertex1 = f"{combined_mesh}.vtx[{destination_vertex1_id}]"
        destination_vertex2 = f"{combined_mesh}.vtx[{destination_vertex2_id}]"
        destination_vertex3 = f"{combined_mesh}.vtx[{destination_vertex3_id}]"
        mel.eval(f"meshRemap {source_vertex1} {source_vertex2} {source_vertex3} {destination_vertex1} {destination_vertex2} {destination_vertex3}")                       

        # Symmetrize
        if self.input_make_symmetric:
            print("symmetrizing...")
            self.symmetrize("combined")
            self.symmetrize("eyes")
            self.symmetrize("teeth")
            self.symmetrize_eyelashes()
        
        # Swap for meshes with polygroups
        for mesh in ["combined", "eyes", "eyelashes", "teeth"]:
            pg_mesh = "pgs:" + mesh
            # Blendshape
            cmds.select(mesh, r=True)
            cmds.select(pg_mesh, add=True)
            blendshape = cmds.blendShape(tc=0)[0]
            cmds.setAttr(f"{blendshape}.{mesh}", 1)
            cmds.select(pg_mesh, r=True)
            cmds.DeleteHistory()
            cmds.select(cl=True)
            # Replace
            cmds.delete(mesh)
            cmds.rename(pg_mesh, mesh)

        # Create folders
        name = self.input_metahuman_folder.split("/")[-1]
        new_objs_folder = f"{self.input_metahuman_folder}/new_OBJs"
        old_objs_folder = f"{self.input_metahuman_folder}/old_OBJs"
        if not os.path.exists(new_objs_folder):
            os.makedirs(new_objs_folder)  
        if not os.path.exists(old_objs_folder):
            os.makedirs(old_objs_folder)

        # Export
        if not cmds.pluginInfo("objExport.mll", query=True, loaded=True): cmds.loadPlugin("objExport.mll")
        for mesh in combined_meshes:
            # File names
            new_obj_file = f"{new_objs_folder}/new_{mesh}.obj"
            if mesh == "eyelashes": new_obj_file = f"{new_objs_folder}/optional_new_{mesh}.obj"
            if mesh == "teeth": new_obj_file = f"{new_objs_folder}/optional_new_{mesh}.obj"
            old_obj_file = f"{old_objs_folder}/old_{mesh}.obj"
            cmds.select(mesh)   
            cmds.file(new_obj_file, f=True, options="groups=1;ptgroups=0;materials=0;smoothing=0;normals=0", type="OBJexport", es=True)
            shutil.copyfile(new_obj_file, old_obj_file)

        # Copy utilities
        head_texture = os.path.dirname(__file__) + "/resources/headT.png"
        head_texture_destination = f"{old_objs_folder}/texture_head.png"
        body_texture = os.path.dirname(__file__) + "/resources/bodyT.png"
        body_texture_destination = f"{old_objs_folder}/texture_body.png"
        shutil.copyfile(head_texture, head_texture_destination)
        shutil.copyfile(body_texture, body_texture_destination)

        # New scene
        cmds.file(new=True, force=True)
        cmds.scriptEditorInfo(suppressWarnings=original_warning_state)

class ObjToMetahuman:
    
    def __init__(self, input_combined_obj, input_eyes_obj, input_eyelashes_obj, input_teeth_obj, input_metahuman_folder):

        # Parameters   
        self.input_combined_obj = input_combined_obj
        self.input_eyes_obj = input_eyes_obj
        self.input_eyelashes_obj = input_eyelashes_obj
        self.input_teeth_obj = input_teeth_obj
        self.input_head_dna = input_metahuman_folder + "/head.dna"
        self.input_body_dna = input_metahuman_folder + "/body.dna"
        self.input_metahuman_folder = input_metahuman_folder

        # Run
        original_warning_state = cmds.scriptEditorInfo(query=True, suppressWarnings=True)
        cmds.scriptEditorInfo(suppressWarnings=True)

        self.print_parameters()
        self.run()    
        #self.debug()

        cmds.scriptEditorInfo(suppressWarnings=original_warning_state)
    
    def print_parameters(self):
        print(f"combined: {self.input_combined_obj}")
        print(f"eyes: {self.input_eyes_obj}")
        print(f"eyelashes: {self.input_eyelashes_obj}")
        print(f"teeth: {self.input_teeth_obj}")
        print(f"head dna: {self.input_head_dna}")
        print(f"body dna: {self.input_body_dna}")
        print(f"metahuman folder: {self.input_metahuman_folder}")
    
    def print_mesh_element(self, mesh_element):
        print(f"{mesh_element.name}")
        print(f"  index: {mesh_element.index}")
        print(f"  lod: {mesh_element.lod}")
        print(f"  poly_faces: {mesh_element.poly_faces}")
        print(f"  poly_connections: {mesh_element.poly_connections}")
        print("")
    
    def load_dna(self):
        # Necessary group when creating meshes and joints from dna
        cmds.group(empty=True, name="head_grp")
            
        # Create dna objects
        head_input_stream = FileStream(self.input_head_dna, AccessMode_Read, OpenMode_Binary)
        body_input_stream = FileStream(self.input_body_dna, AccessMode_Read, OpenMode_Binary)
        head_reader = BinaryStreamReader(head_input_stream, DataLayer_All)
        body_reader = BinaryStreamReader(body_input_stream, DataLayer_All)
        head_reader.read()
        body_reader.read()
        head_dna_object = DNA(self.input_head_dna, head_reader)
        body_dna_object = DNA(self.input_body_dna, body_reader)
        print(self.input_head_dna)
        print(self.input_body_dna)
        print(head_dna_object)
        print(body_dna_object)
        
        for dna_object in [head_dna_object, body_dna_object]:
            # Construct maya mesh handler
            form = ProcessForm()
            maya_config = MayaConfig()
            maya_mesh_handler = MayaMeshHandler(dna_object, form, maya_config)
            mesh_element = dna_object.get_mesh(0)
            mesh_elements = dna_object.get_meshes()

            # Add meshes to scene
            dna_meshes = []
            for element in mesh_elements:
                #skip_names = ["saliva", "eyeshell", "eyeEdge", "cartilage"]
                #if element.lod == 0 and not any(name in element.name for name in skip_names):
                if element.lod == 0:
                    maya_mesh_handler.add_mesh_to_scene(element)
                    maya_mesh_handler.add_mesh_uv(element)
                    maya_mesh_handler.add_mesh_shader(element)
                    dna_meshes.append(element.name)
            if dna_object == head_dna_object: head_dna_meshes = dna_meshes.copy()
            if dna_object == body_dna_object: body_dna_meshes = dna_meshes.copy()

            # Add joints
            maya_joint_handler = MayaJointHandler(dna_object, form, maya_config)
            maya_joint_handler.create_joints()
            #maya_skinweights_handler = MayaSkinWeightsHandler(dna_object, form, maya_config)
            #maya_skinweights_handler.create_skin_weights([mesh_element])
            
            # Place joints in their namespace
            if dna_object == head_dna_object:
                cmds.namespace(addNamespace="old_head")
                cmds.select("spine_04", hi=True)
                for item in cmds.ls(sl=True): cmds.rename(item, f"old_head:{item}")        
                old_head_joints = cmds.ls(sl=True)
            if dna_object == body_dna_object:
                cmds.namespace(addNamespace="old_body")
                cmds.select("root", hi=True)
                for item in cmds.ls(sl=True): cmds.rename(item, f"old_body:{item}")
                old_body_joints = cmds.ls(sl=True)
        
        # Place meshes in their namespace
        for i, item in enumerate(head_dna_meshes): 
            cmds.rename(item, f"old_head:{item}")
            head_dna_meshes[i] = f"old_head:{item}"
        for i, item in enumerate(body_dna_meshes): 
            cmds.rename(item, f"old_body:{item}")
            body_dna_meshes[i] = f"old_body:{item}"

        # Create old combined
        cmds.namespace(add=":old")
        head = cmds.duplicate("old_head:head_lod0_mesh", name="old:head_lod0_mesh")[0]
        body = cmds.duplicate("old_body:body_lod0_mesh", name="old:body_lod0_mesh")[0]
        cmds.polyUnite([head, body], name="old:combined", ch=False)
        cmds.polyMergeVertex(['old:combined.vtx[2805:2824]', 'old:combined.vtx[2873]', 'old:combined.vtx[2876]', 'old:combined.vtx[2965]', 'old:combined.vtx[2997]', 'old:combined.vtx[5876:5895]', 'old:combined.vtx[5944]', 'old:combined.vtx[5947]', 'old:combined.vtx[11560]', 'old:combined.vtx[11564]', 'old:combined.vtx[11567]', 'old:combined.vtx[11569]', 'old:combined.vtx[11572]', 'old:combined.vtx[11575]', 'old:combined.vtx[11578]', 'old:combined.vtx[11582]', 'old:combined.vtx[11585]', 'old:combined.vtx[11587]', 'old:combined.vtx[11600]', 'old:combined.vtx[11795]', 'old:combined.vtx[11798:11799]', 'old:combined.vtx[11802:11803]', 'old:combined.vtx[11805]', 'old:combined.vtx[11807]', 'old:combined.vtx[11809]', 'old:combined.vtx[11811]', 'old:combined.vtx[11899]', 'old:combined.vtx[11909:11910]', 'old:combined.vtx[17607]', 'old:combined.vtx[17610]', 'old:combined.vtx[17614]', 'old:combined.vtx[17617]', 'old:combined.vtx[17619]', 'old:combined.vtx[17622]', 'old:combined.vtx[17626]', 'old:combined.vtx[17629]', 'old:combined.vtx[17632]', 'old:combined.vtx[17635]', 'old:combined.vtx[17647]', 'old:combined.vtx[17854]', 'old:combined.vtx[17856]', 'old:combined.vtx[17859:17860]', 'old:combined.vtx[17863]', 'old:combined.vtx[17865]', 'old:combined.vtx[17867]', 'old:combined.vtx[17869]', 'old:combined.vtx[17871]', 'old:combined.vtx[17962]', 'old:combined.vtx[17968]', 'old:combined.vtx[17972]', 'old:combined.vtx[24049:24093]', 'old:combined.vtx[27867]', 'old:combined.vtx[31694]', 'old:combined.vtx[33235]', 'old:combined.vtx[33241]', 'old:combined.vtx[33244]', 'old:combined.vtx[33247]', 'old:combined.vtx[33252]', 'old:combined.vtx[33255:33256]', 'old:combined.vtx[33260]', 'old:combined.vtx[37976]', 'old:combined.vtx[37980]', 'old:combined.vtx[38004]', 'old:combined.vtx[38006:38007]', 'old:combined.vtx[38009]', 'old:combined.vtx[38011]', 'old:combined.vtx[38013]', 'old:combined.vtx[38015]', 'old:combined.vtx[38017]', 'old:combined.vtx[39207]', 'old:combined.vtx[39219]', 'old:combined.vtx[39229]', 'old:combined.vtx[39238]', 'old:combined.vtx[39276]', 'old:combined.vtx[40823:40824]', 'old:combined.vtx[40828]', 'old:combined.vtx[40833]', 'old:combined.vtx[40835]', 'old:combined.vtx[40838]', 'old:combined.vtx[40843:40844]', 'old:combined.vtx[45589]', 'old:combined.vtx[45591]', 'old:combined.vtx[45613]', 'old:combined.vtx[45615]', 'old:combined.vtx[45618]', 'old:combined.vtx[45620]', 'old:combined.vtx[45622]', 'old:combined.vtx[45624]', 'old:combined.vtx[45626:45627]', 'old:combined.vtx[46850]', 'old:combined.vtx[46863]', 'old:combined.vtx[46873]', 'old:combined.vtx[46882]'], d=0.01, am=1, ch=0)
        cmds.select(cl=True)
        cmds.reorder("old:combined", f=True)
        cmds.reorder("old:combined", r=4)

        # Clean up
        cmds.parent("old_head:spine_04", world=True)
        cmds.reorder("old_head:spine_04", r=-1)
        cmds.parent("old_body:root", world=True)
        cmds.delete("head_grp")
        cmds.select(cl=True)

        return
    
    def prepare_fitting_drivers(self):
        cmds.namespace(add=":driver")
        cmds.namespace(set=":driver")
        drivers_file = os.path.dirname(__file__) + "/resources/drivers.fbx"
        cmds.file(drivers_file, i=True, f=True)
        cmds.namespace(add=":driver_target")
        cmds.namespace(set=":driver_target")
        drivers = cmds.ls("driver:*", et="transform")
        for driver in drivers:
            cmds.setAttr(f"{driver}.v", False)
            target = cmds.duplicate(driver)[0]
            if "mouth" in driver:
                reference_mesh = "head_lod0_mesh"
                reference_vertex_ids = resources.data.mouth_reference_vertex_ids
            if "cartilage" in driver:
                reference_mesh = "head_lod0_mesh"
                reference_vertex_ids = resources.data.cartilage_reference_vertex_ids
            if "eyeCorners" in driver:
                reference_mesh = "head_lod0_mesh"
                reference_vertex_ids = resources.data.eyeCorners_reference_vertex_ids
            if "eyeLeft" in driver:
                reference_mesh = "eyeLeft_lod0_mesh"
                reference_vertex_ids = resources.data.eyeLeft_reference_vertex_ids
            if "eyeRight" in driver:
                reference_mesh = "eyeRight_lod0_mesh"
                reference_vertex_ids = resources.data.eyeRight_reference_vertex_ids
            snap_vertices(driver, f"old_head:{reference_mesh}", reference_vertex_ids)
            snap_vertices(target, f"new_head:{reference_mesh}", reference_vertex_ids)  
            bs = cmds.blendShape(target, driver)[0]
            cmds.setAttr(f"{bs}.{om2.MNamespace.stripNamespaceFromName(target)}", 1)
    
    def create_shrink_wrap(self, mesh, target, name="shrinkWrap1", **kwargs):
        """
        Check available kwargs with parameters below.
        """
        parameters = [
            ("projection", 2),
            ("closestIfNoIntersection", 1),
            ("reverse", 0),
            ("bidirectional", 1),
            ("boundingBoxCenter", 1),
            ("axisReference", 1),
            ("alongX", 0),
            ("alongY", 0),
            ("alongZ", 1),
            ("offset", 0),
            ("targetInflation", 0),
            ("targetSmoothLevel", 0),
            ("falloff", 0),
            ("falloffIterations", 1),
            ("shapePreservationEnable", 0),
            ("shapePreservationSteps", 1)
        ]

        target_shapes = cmds.listRelatives(target, f=True, shapes=True, type="mesh", ni=True)
        if not target_shapes:
            raise ValueError("The target supplied is not a mesh")
        target_shape = target_shapes[0]

        shrink_wrap = cmds.deformer(mesh, type="shrinkWrap", n=name)[0]

        for parameter, default in parameters:
            cmds.setAttr(
                shrink_wrap + "." + parameter,
                kwargs.get(parameter, default))

        connections = [
            ("worldMesh", "targetGeom"),
            ("continuity", "continuity"),
            ("smoothUVs", "smoothUVs"),
            ("keepBorder", "keepBorder"),
            ("boundaryRule", "boundaryRule"),
            ("keepHardEdge", "keepHardEdge"),
            ("propagateEdgeHardness", "propagateEdgeHardness"),
            ("keepMapBorders", "keepMapBorders")
        ]

        for out_plug, in_plug in connections:
            cmds.connectAttr(
                target_shape + "." + out_plug,
                shrink_wrap + "." + in_plug)

        return shrink_wrap

    def generate_missing_new_mesh(self, old_mesh):
        new_mesh = old_mesh.replace("old", "new")
        cmds.namespace(set=":")
        cmds.duplicate(old_mesh, name=new_mesh)
        if "teeth" in new_mesh:
            pw = cmds.proximityWrap(new_mesh)[0]
            cmds.proximityWrap(pw, edit=True, addDrivers="driver:mouth")
            cmds.setAttr(f"{pw}.wrapMode", 0)
            cmds.setAttr(f"{pw}.falloffScale", 10)
            cmds.deltaMush(new_mesh, smoothingIterations=10, smoothingStep=0.5)

        if "saliva" in new_mesh:
            pw = cmds.proximityWrap(new_mesh)[0]
            cmds.proximityWrap(pw, edit=True, addDrivers="driver:mouth")
            cmds.setAttr(f"{pw}.wrapMode", 0)
            cmds.setAttr(f"{pw}.falloffScale", 10)
            cmds.deltaMush(new_mesh, smoothingIterations=10, smoothingStep=0.5)

        if "eyeshell" in new_mesh:
            pw = cmds.proximityWrap(new_mesh)[0]
            cmds.proximityWrap(pw, edit=True, addDrivers="driver:eyeCorners")
            cmds.setAttr(f"{pw}.wrapMode", 0)
            cmds.setAttr(f"{pw}.falloffScale", 10)
            cmds.deltaMush(new_mesh, smoothingIterations=10, smoothingStep=0.5)

        if "eyelashes" in new_mesh:
            pw = cmds.proximityWrap(new_mesh)[0]
            cmds.proximityWrap(pw, edit=True, addDrivers="driver:cartilage")
            cmds.setAttr(f"{pw}.wrapMode", 0)
            cmds.setAttr(f"{pw}.falloffScale", 10)
            cmds.deltaMush(new_mesh, smoothingIterations=10, smoothingStep=0.5)

        if "eyeEdge" in new_mesh:
            pw = cmds.proximityWrap(new_mesh)[0]
            cmds.proximityWrap(pw, edit=True, addDrivers="driver:eyeCorners")
            cmds.setAttr(f"{pw}.wrapMode", 0)
            cmds.setAttr(f"{pw}.smoothInfluences", 10)
            shape_orig = cmds.listConnections(f"{pw}.originalGeometry", p=True, source=True)[0].split(".")[0]
            
            # Add eyeCorners shrink
            eyeCorners_shrink = self.create_shrink_wrap(new_mesh, "driver:eyeCorners", name="eyeCorners_shrink", projection=4, closestIfNoIntersection=0)
            vertex_ids = [14, 16, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 52, 67, 68, 69, 70, 71, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 103, 141, 147, 153, 154, 165, 171, 172, 178, 179, 180, 181, 182, 183, 184, 185, 188, 191, 194, 197, 200, 203, 206, 209, 212, 215, 218, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 233, 236, 239, 242, 245, 248, 251, 254, 257, 260, 263, 266, 267]
            #shape_orig = cmds.listConnections(f"{eyeCorners_shrink}.originalGeometry", p=True, source=True)[0].split(".")[0]
            shape_orig_vertex_id_names = []
            for id in vertex_ids: shape_orig_vertex_id_names.append(f"{shape_orig}.vtx[{id}]")                
            cmds.componentTag(shape_orig_vertex_id_names, cr=True, ntn="eyeCorners_shrink")
            cmds.connectAttr(f"{shape_orig}.componentTags[0].componentTagName", f"{eyeCorners_shrink}.input[0].componentTagExpression", f=True)
            cmds.setAttr(f"{eyeCorners_shrink}.offset", 0.0)

            # Add eyeLeft shrink
            eyeLeft_shrink = self.create_shrink_wrap(new_mesh, "driver:eyeLeft", name="eyeLeft_shrink", projection=4, closestIfNoIntersection=0)
            vertex_ids = [0, 1, 2, 3, 4, 5, 6, 7, 17, 18, 19, 20, 21, 22, 51, 53, 54, 55, 56, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 231, 232, 234, 235, 237, 238, 240, 241, 243, 244, 246, 247, 249, 250, 252, 253, 255, 256, 258, 259, 261, 262, 264, 265]
            #shape_orig = cmds.listConnections(f"{eyeLeft_shrink}.originalGeometry", p=True, source=True)[0].split(".")[0]
            shape_orig_vertex_id_names = []
            for id in vertex_ids: shape_orig_vertex_id_names.append(f"{shape_orig}.vtx[{id}]")                
            cmds.componentTag(shape_orig_vertex_id_names, cr=True, ntn="eyeLeft_shrink")
            cmds.connectAttr(f"{shape_orig}.componentTags[1].componentTagName", f"{eyeLeft_shrink}.input[0].componentTagExpression", f=True)
            cmds.setAttr(f"{eyeLeft_shrink}.offset", 0.01)

            # Add eyeRight shrink
            eyeRight_shrink = self.create_shrink_wrap(new_mesh, "driver:eyeRight", name="eyeRight_shrink", projection=4, closestIfNoIntersection=0)
            vertex_ids = [57, 58, 59, 60, 61, 62, 63, 64, 72, 73, 74, 75, 76, 77, 102, 104, 105, 106, 107, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 186, 187, 189, 190, 192, 193, 195, 196, 198, 199, 201, 202, 204, 205, 207, 208, 210, 211, 213, 214, 216, 217, 219, 220]
            #shape_orig = cmds.listConnections(f"{eyeRight_shrink}.originalGeometry", p=True, source=True)[0].split(".")[0]
            shape_orig_vertex_id_names = []
            for id in vertex_ids: shape_orig_vertex_id_names.append(f"{shape_orig}.vtx[{id}]")                
            cmds.componentTag(shape_orig_vertex_id_names, cr=True, ntn="eyeRight_shrink")
            cmds.connectAttr(f"{shape_orig}.componentTags[2].componentTagName", f"{eyeRight_shrink}.input[0].componentTagExpression", f=True)
            cmds.setAttr(f"{eyeRight_shrink}.offset", 0.01)

        if "cartilage" in new_mesh:
            pw = cmds.proximityWrap(new_mesh)[0]
            cmds.proximityWrap(pw, edit=True, addDrivers="driver:cartilage")
            cmds.setAttr(f"{pw}.wrapMode", 0)
            cmds.setAttr(f"{pw}.smoothInfluences", 1)

        cmds.select(new_mesh)
        cmds.DeleteHistory()
        cmds.select(cl=True)
    
    def load_new_meshes(self):
        # Load obj plugin
        cmds.loadPlugin("objExport.mll")
        
        # New namespaces
        cmds.namespace(add=":temp")
        cmds.namespace(add=":new")
        cmds.namespace(add=":new_head")
        cmds.namespace(add=":new_body")

        # Import eyes and separate
        cmds.namespace(set=":temp")
        cmds.file(self.input_eyes_obj, i=True, options="mo=0")
        cmds.namespace(set=":")
        aux = cmds.ls("temp:*", et="transform")
        items = cmds.polySeparate(aux[0], ch=False)
        for item in items:
            cmds.select(item)
            cmds.DeleteHistory()
            cmds.parent(item, world=True)
        cmds.rename(items[0], "new_head:eyeLeft_lod0_mesh")
        cmds.rename(items[1], "new_head:eyeRight_lod0_mesh")  
        cmds.delete(cmds.ls("temp:*"))
        
        # Import combined
        cmds.namespace(set=":temp")
        cmds.file(self.input_combined_obj, i=True, options="mo=0")
        cmds.namespace(set=":")
        cmds.rename(cmds.ls("temp:*", type="transform")[0], "new:combined")
        cmds.reorder("new:combined", r=-2)
        # Create head by duplicating combined and deleting body faces
        cmds.duplicate("new:combined", name="new_head:head_lod0_mesh")
        cmds.select("new_head:head_lod0_mesh.f[24002:54409]")
        cmds.delete()
        cmds.reorder("new_head:head_lod0_mesh", r=-2)
        # Create body by duplicating combined, deleting head faces and reordering vertices
        cmds.duplicate("new:combined", name="new_body:body_lod0_mesh")
        cmds.select("new_body:body_lod0_mesh.f[0:24001]")
        cmds.delete()
        cmds.namespace(set=":temp")
        aux = os.path.dirname(__file__) + "/resources/metahuman_body.fbx"
        cmds.file(aux, i=True, f=True)
        cmds.namespace(set=":")
        cmds.loadPlugin("meshReorder.mll")
        source_vertex1 = "temp:body_lod0_mesh.vtx[0]"
        source_vertex2 = "temp:body_lod0_mesh.vtx[9204]"
        source_vertex3 = "temp:body_lod0_mesh.vtx[27330]"
        destination_vertex1 = "new_body:body_lod0_mesh.vtx[8]"
        destination_vertex2 = "new_body:body_lod0_mesh.vtx[9244]"
        destination_vertex3 = "new_body:body_lod0_mesh.vtx[27330]"
        mel.eval(f"meshRemap {source_vertex1} {source_vertex2} {source_vertex3} {destination_vertex1} {destination_vertex2} {destination_vertex3}")                       
        cmds.delete(cmds.ls("temp:*"))

        # Import eyelashes if available
        if self.input_eyelashes_obj != "auto generated": 
            cmds.namespace(set=":temp")
            cmds.file(self.input_eyelashes_obj, i=True, options="mo=0")
            cmds.namespace(set=":")
            cmds.rename(cmds.ls("temp:*", type="transform")[0], "new_head:eyelashes_lod0_mesh")
            cmds.reorder("new_head:eyelashes_lod0_mesh", r=-1)
            cmds.delete(cmds.ls("temp:*"))
        
        # Import teeth if available
        if self.input_teeth_obj != "auto generated": 
            cmds.namespace(set=":temp")
            cmds.file(self.input_teeth_obj, i=True, options="mo=0")
            cmds.namespace(set=":")
            cmds.rename(cmds.ls("temp:*", type="transform")[0], "new_head:teeth_lod0_mesh")
            cmds.reorder("new_head:teeth_lod0_mesh", r=-1)
            cmds.delete(cmds.ls("temp:*"))
    
        # Generate missing new meshes
        old_head_meshes = cmds.ls("old_head:*", et="transform")
        old_body_meshes = cmds.ls("old_body:*", et="transform")
        new_head_meshes = cmds.ls("new_head:*", et="transform")
        new_body_meshes = cmds.ls("new_body:*", et="transform")
        drivers_prepared = False
        
        for old_meshes in [old_head_meshes, old_body_meshes]:     
            if old_meshes == old_head_meshes: new_meshes = new_head_meshes
            if old_meshes == old_body_meshes: new_meshes = new_body_meshes   
            for old_mesh in old_meshes:
                new_mesh = old_mesh.replace("old", "new")
                # If new mesh is missing...
                if new_mesh not in new_meshes:
                    # Prepare fitting drivers if not already prepared
                    if not drivers_prepared:
                        self.prepare_fitting_drivers()
                        drivers_prepared = True
                    # Generate missing new mesh
                    self.generate_missing_new_mesh(old_mesh)

        # Fitting cleanup
        if drivers_prepared:
            cmds.delete(cmds.ls("driver:*"))
            cmds.delete(cmds.ls("driver_target:*"))
            cmds.namespace(rm=":driver")
            cmds.namespace(rm=":driver_target")

    def create_matrix_from_vectors(self, tangent, bitangent, normal, position):
        # Create an MMatrix and fill it with the correct values
        matrix = om2.MMatrix()

        matrix.setElement(0, 0, tangent.x)
        matrix.setElement(0, 1, tangent.y)
        matrix.setElement(0, 2, tangent.z)
        matrix.setElement(0, 3, 0)

        matrix.setElement(1, 0, bitangent.x)
        matrix.setElement(1, 1, bitangent.y)
        matrix.setElement(1, 2, bitangent.z)
        matrix.setElement(1, 3, 0)

        matrix.setElement(2, 0, normal.x)
        matrix.setElement(2, 1, normal.y)
        matrix.setElement(2, 2, normal.z)
        matrix.setElement(2, 3, 0)

        matrix.setElement(3, 0, position.x)
        matrix.setElement(3, 1, position.y)
        matrix.setElement(3, 2, position.z)
        matrix.setElement(3, 3, 1)
        return matrix

    def get_vertex_space(self, vertex_iterator):
        position = vertex_iterator.position(om2.MSpace.kWorld)
        connected_vertices = vertex_iterator.getConnectedVertices()
        vertex_iterator.setIndex(connected_vertices[0])
        v0_position = vertex_iterator.position(om2.MSpace.kWorld)
        vertex_iterator.setIndex(connected_vertices[1])
        v1_position = vertex_iterator.position(om2.MSpace.kWorld)
        vector_x = om2.MVector(v0_position - position)
        vector_y = om2.MVector(v1_position - position)
        vector_z = (vector_x ^ vector_y)
        vector_z = vector_z * (math.sqrt(vector_z.length()) / vector_z.length())
        matrix = self.create_matrix_from_vectors(vector_x, vector_y, vector_z, position)
        return matrix
    
    def get_closest_vertex_to_position(self, position, mesh, valid_vertex_ids = None):
        vertex_positions = mesh.getPoints(om2.MSpace.kWorld)        
        closest_vertex_distance = 99999999

        if valid_vertex_ids == None:
            mesh_vertex_iterator = om2.MItMeshVertex(mesh.dagPath())
            while not mesh_vertex_iterator.isDone():
                vertex_id = mesh_vertex_iterator.index()
                vertex_position = vertex_positions[vertex_id]
                distance = vertex_position.distanceTo(position)
                if distance < closest_vertex_distance:
                    closest_vertex_id = vertex_id
                    closest_vertex_position = vertex_position
                    closest_vertex_distance = distance
                mesh_vertex_iterator.next()
        else:
            for vertex_id in valid_vertex_ids:
                vertex_position = vertex_positions[vertex_id]
                distance = vertex_position.distanceTo(position)
                if distance < closest_vertex_distance:
                    closest_vertex_id = vertex_id
                    closest_vertex_position = vertex_position
                    closest_vertex_distance = distance

        return closest_vertex_id, closest_vertex_position, closest_vertex_distance
    
    def get_reference_vertex_ids(self, mesh, cull_distance_multiplier, vertex_iterator, reference_position, valid_vertex_ids):
        
        closest_vertex_id, closest_vertex_position, closest_vertex_distance = self.get_closest_vertex_to_position(reference_position, mesh, valid_vertex_ids)
        cull_distance = closest_vertex_distance * cull_distance_multiplier
        reference_vertex_ids = []
        vertex_positions = mesh.getPoints(om2.MSpace.kWorld)
        for vertex_id in valid_vertex_ids:
            vertex_position = vertex_positions[vertex_id]
            distance = reference_position.distanceTo(vertex_position)
            if distance <= cull_distance: reference_vertex_ids.append(vertex_id)
        return reference_vertex_ids, closest_vertex_id
    
    def match_joint(self, joints_info, source_space_vertex_iterator, target_space_vertex_iterator, source_joint_dag_path, target_joint_dag_path):
        joint = om2.MNamespace.stripNamespaceFromName(str(target_joint_dag_path))
        reference_vertex_ids = joints_info[joint]["reference_vertex_ids"]
        
        if reference_vertex_ids:
            #print(f"matching joint {target_joint_dag_path} using {len(reference_vertex_ids)} reference_vertex_ids:\n{reference_vertex_ids}\n")
            source_joint_inclusive_matrix = source_joint_dag_path.inclusiveMatrix()
            source_joint_world_position = om2.MPoint(cmds.xform(source_joint_dag_path, query=True, translation=True, worldSpace=True))

            # Get weighted matrices for each sample vertex
            added_matrix = om2.MMatrix() * 0
            total_weight = 0
            for vertex_id in reference_vertex_ids:
                source_space_vertex_iterator.setIndex(vertex_id)
                target_space_vertex_iterator.setIndex(vertex_id)
                # Get weight
                distance = source_joint_world_position.distanceTo(source_space_vertex_iterator.position())
                if distance == 0: distance = 0.001
                weight = 1 / pow(distance, 2)
                total_weight = total_weight + weight
                # Get matrix
                source_space_vertex_matrix = self.get_vertex_space(source_space_vertex_iterator)
                target_space_vertex_matrix = self.get_vertex_space(target_space_vertex_iterator)
                matrix = source_joint_inclusive_matrix * source_space_vertex_matrix.inverse() * target_space_vertex_matrix
                added_matrix += matrix * weight

            # Get average matrix
            matrix = added_matrix * (1 / total_weight)

            # Set target joint transformation
            #matrix_transformation = om2.MTransformationMatrix(source_joint_inclusive_matrix)
            matrix_transformation = om2.MTransformationMatrix(matrix)
            target_joint_transform = om2.MFnTransform(target_joint_dag_path)
            target_joint_transform.setTransformation(matrix_transformation)

            # Change rotation for joint orient
            cmds.setAttr(f"{target_joint_dag_path}.jointOrientX", cmds.getAttr(f"{target_joint_dag_path}.rotateX"))
            cmds.setAttr(f"{target_joint_dag_path}.jointOrientY", cmds.getAttr(f"{target_joint_dag_path}.rotateY"))
            cmds.setAttr(f"{target_joint_dag_path}.jointOrientZ", cmds.getAttr(f"{target_joint_dag_path}.rotateZ"))
            cmds.setAttr(f"{target_joint_dag_path}.rotateX", 0)
            cmds.setAttr(f"{target_joint_dag_path}.rotateY", 0)
            cmds.setAttr(f"{target_joint_dag_path}.rotateZ", 0)
            cmds.setAttr(f"{target_joint_dag_path}.scaleX", 1)
            cmds.setAttr(f"{target_joint_dag_path}.scaleY", 1)
            cmds.setAttr(f"{target_joint_dag_path}.scaleZ", 1)  
    
    def fix_head_skeleton(self, joints_info):
        dagpath = om2.MSelectionList().add("new_head:spine_04").getDagPath(0)
        dag_iterator = om2.MItDag().reset(dagpath)
        while not dag_iterator.isDone():
            joint = dag_iterator.partialPathName()
            joint_basename = om2.MNamespace.stripNamespaceFromName(joint)
            if "follow=" in joints_info[joint_basename]["world_position"][0]:
                # Unparent from parent
                has_parent = cmds.listRelatives(joint, parent=True)
                if has_parent:
                    parent = has_parent[0]
                    cmds.parent(joint, w=True)

                # Unparent children
                children = cmds.listRelatives(joint, children=True)
                if children: cmds.parent(children, w=True)

                # Follow joint position
                followed_joint = joints_info[joint_basename]["world_position"][0].split("=")[1]
                followed_position = cmds.xform(followed_joint, query=True, translation=True, worldSpace=True)
                cmds.xform(joint, t=followed_position, ws=True)

                # Re-parent to parent
                if has_parent: cmds.parent(joint, parent)
                
                # Re-parent children
                if children: cmds.parent(children, joint)

            if "follow=" in joints_info[joint_basename]["world_orientation"]:
                # Unparent from parent
                has_parent = cmds.listRelatives(joint, parent=True)
                if has_parent:
                    parent = has_parent[0]
                    cmds.parent(joint, w=True)

                # Unparent children
                children = cmds.listRelatives(joint, children=True)
                if children: cmds.parent(children, w=True)

                # Follow joint orientation
                followed_joint = joints_info[joint_basename]["world_orientation"].split("=")[1]
                followed_joint_has_parent = cmds.listRelatives(followed_joint, parent=True)
                if followed_joint_has_parent:
                    followed_joint_parent = followed_joint_has_parent[0]
                    cmds.parent(followed_joint, w=True)
                orientation = cmds.joint(followed_joint, q=True, o=True)
                cmds.joint(joint, edit=True, o=(orientation[0], orientation[1], orientation[2]))
                if followed_joint_has_parent: cmds.parent(followed_joint, followed_joint_parent)

                # Re-parent to parent
                if has_parent: cmds.parent(joint, parent)
                
                # Re-parent children
                if children: cmds.parent(children, joint)                

            dag_iterator.next()
    
    def fix_body_skeleton(self, namespace=":", source_namespace=":"):
        body_joints_file = os.path.dirname(__file__) + "/resources/body_joints.json"
        joints_info = json.load(open(body_joints_file, "r"))
        root = namespace + "root"
        root_dagpath = om2.MSelectionList().add(root).getDagPath(0)
        dag_iterator = om2.MItDag()
        
        # Position pass
        dag_iterator.reset(root_dagpath, filterType=om2.MFn.kJoint)
        while not dag_iterator.isDone():
            joint = dag_iterator.partialPathName()
            #print(f"fixing position for joint: {joint}")
            joint_info = joints_info[om2.MNamespace.stripNamespaceFromName(joint)]
            if joint_info["parent"]: parent = namespace + joint_info["parent"]
            if joint_info["child"]: child = namespace + joint_info["child"]
            
            # Unparent from parent
            if joint_info["parent"]: cmds.parent(joint, w=True)

            # Unparent children
            children = cmds.listRelatives(joint, children=True)
            if children: cmds.parent(children, w=True)
            #print("checking joint: ", joint)

            # Fix twists
            if joint_info["world_position"][0] == "twist":
                parent_child = namespace + joints_info[om2.MNamespace.stripNamespaceFromName(parent)]["child"]
                constraint = cmds.parentConstraint(parent, parent_child, joint, weight=1)
                if any(text in joint for text in ["upperarm_twist_01", "lowerarm_twist_02", "thigh_twist_01", "calf_twist_02"]):
                    cmds.setAttr(f"{constraint[0]}.{om2.MNamespace.stripNamespaceFromName(parent)}W0", 0.6667)
                    cmds.setAttr(f"{constraint[0]}.{om2.MNamespace.stripNamespaceFromName(parent_child)}W1", 0.3333)
                else:
                    cmds.setAttr(f"{constraint[0]}.{om2.MNamespace.stripNamespaceFromName(parent)}W0", 0.3333)
                    cmds.setAttr(f"{constraint[0]}.{om2.MNamespace.stripNamespaceFromName(parent_child)}W1", 0.6667)
                cmds.delete(constraint)
                cmds.setAttr(f"{joint}.rotate", 0, 0, 0) 
            
            # If not twist
            else:
                for i, axis in enumerate(["X", "Y", "Z"]):
                    mode = joint_info["world_position"][i]
                    if mode == "0":
                        #print(f"setting {joint}.translate{axis} to 0")
                        cmds.setAttr(f"{joint}.translate{axis}", 0)
                    elif mode == "parent":
                        parent_position = cmds.xform(parent, query=True, translation=True, worldSpace=True)[i]
                        cmds.setAttr(f"{joint}.translate{axis}", parent_position)
                        #print(f"setting {joint}.translate{axis} to parent")

            # Re-parent to parent
            if joint_info["parent"]: cmds.parent(joint, parent)
            
             # Re-parent children
            if children: cmds.parent(children, joint)

            dag_iterator.next()

        # Orientation pass
        dag_iterator.reset(root_dagpath, filterType=om2.MFn.kJoint)
        while not dag_iterator.isDone():
            joint = dag_iterator.partialPathName()
            #print(f"fixing orientation for joint: {joint}")
            joint_info = joints_info[om2.MNamespace.stripNamespaceFromName(joint)]
            if joint_info["parent"]: parent = namespace + joint_info["parent"]
            if joint_info["child"]: main_child = namespace + joint_info["child"]
            source_joint = source_namespace + om2.MNamespace.stripNamespaceFromName(joint)
            children = cmds.listRelatives(joint, children=True)
            
            # Make sure rotate is [0, 0, 0]
            cmds.setAttr(f"{joint}.rotate", 0, 0, 0)

            # Joint orients
            if joint_info["orientation"] == "-90, 0, 0 in LS": # hands
                if children: cmds.parent(children, world=True)
                cmds.setAttr(f"{joint}.jointOrient", -90, 0, 0)
                if children: cmds.parent(children, joint)

            elif joint_info["orientation"] == "0, 0, 0":
                if children: cmds.parent(children, world=True)
                cmds.setAttr(f"{joint}.jointOrient", 0, 0, 0)
                if children: cmds.parent(children, joint)
        
            elif joint_info["orientation"] == "copy source":
                if children: cmds.parent(children, world=True)
                source_joint_orientation = cmds.getAttr(f"{source_joint}.jointOrient")[0]
                cmds.setAttr(f"{joint}.jointOrient", source_joint_orientation[0], source_joint_orientation[1], source_joint_orientation[2])
                if children: cmds.parent(children, joint)

            elif joint_info["orientation"] == "+x to child, +y to world -z": # spine, left_arm_up
                cmds.parent(children, world=True)
                cmds.parent(main_child, joint)
                cmds.joint(joint, edit=True, orientJoint="xyz", secondaryAxisOrient="zdown", zeroScaleOrient=True)
                cmds.parent(main_child, world=True)
                cmds.parent(children, joint) 
            
            elif joint_info["orientation"] == "-90, 0, 90 in WS": # head
                cmds.parent(joint, world=True)
                cmds.setAttr(f"{joint}.jointOrient", -90, 0, 90)                    
                cmds.parent(joint, parent)

            elif joint_info["orientation"] == "+x to child, +z to parent^child RH": # left_arm_down
                cmds.parent(children, world=True)
                cmds.parent(joint, world=True)
                cmds.setAttr(f"{joint}.jointOrient", 0, 0, 0) 
                v1 = om2.MVector(om2.MVector(cmds.xform(parent, query=True, t=True, ws=True)) - om2.MVector(cmds.xform(joint, query=True, t=True, ws=True)))
                v2 = om2.MVector(om2.MVector(cmds.xform(main_child, query=True, t=True, ws=True)) - om2.MVector(cmds.xform(joint, query=True, t=True, ws=True)))
                aux = v1 ^ v2
                aim = cmds.aimConstraint(main_child, joint, aimVector=[1, 0, 0], upVector=[0, 0, 1], worldUpType="vector", worldUpVector=aux)[0]
                orientation = cmds.getAttr(f"{joint}.rotate")[0]
                cmds.delete(aim)
                cmds.setAttr(f"{joint}.jointOrient", orientation[0], orientation[1], orientation[2])
                cmds.setAttr(f"{joint}.rotate", 0, 0, 0)
                cmds.parent(joint, parent)
                cmds.parent(children, joint)   
            
            elif joint_info["orientation"] == "+x to child, +z to calculated +z": # left finger, right leg
                print("skip")
                """
                cmds.parent(children, world=True)
                cmds.parent(joint, world=True)
                locator_0 = cmds.spaceLocator()[0]
                locator_z = cmds.spaceLocator()[0]
                cmds.parent([locator_0, locator_z], joint)
                cmds.xform(locator_0, translation=[0, 0, 0])
                cmds.xform(locator_z, translation=[0, 0, 1])
                cmds.parent([locator_0, locator_z], world=True)
                vector_z = om2.MVector(cmds.xform(locator_z, query=True, translation=True)) - om2.MVector(cmds.xform(locator_0, query=True, translation=True))
                cmds.delete([locator_0, locator_z])
                cmds.setAttr(f"{joint}.jointOrient", 0, 0, 0)                        
                aim = cmds.aimConstraint(main_child, joint, aimVector=[1, 0, 0], upVector=[0, 0, 1], worldUpType="vector", worldUpVector=vector_z)[0]
                orientation = cmds.getAttr(f"{joint}.rotate")[0]
                cmds.delete(aim)
                cmds.setAttr(f"{joint}.jointOrient", orientation[0], orientation[1], orientation[2])
                cmds.setAttr(f"{joint}.rotate", 0, 0, 0)
                cmds.parent(joint, parent)
                cmds.parent(children, joint)  
                """

            elif joint_info["orientation"] == "-x to child, +z to calculated +z": # right finger 
                print("skip")
                """
                cmds.parent(children, world=True)
                cmds.parent(joint, world=True)
                locator_0 = cmds.spaceLocator()[0]
                locator_z = cmds.spaceLocator()[0]
                cmds.parent([locator_0, locator_z], joint)
                cmds.xform(locator_0, translation=[0, 0, 0])
                cmds.xform(locator_z, translation=[0, 0, 1])
                cmds.parent([locator_0, locator_z], world=True)
                vector_z = om2.MVector(cmds.xform(locator_z, query=True, translation=True)) - om2.MVector(cmds.xform(locator_0, query=True, translation=True))
                cmds.delete([locator_0, locator_z])
                cmds.setAttr(f"{joint}.jointOrient", 0, 0, 0)                        
                aim = cmds.aimConstraint(main_child, joint, aimVector=[-1, 0, 0], upVector=[0, 0, 1], worldUpType="vector", worldUpVector=vector_z)[0]
                orientation = cmds.getAttr(f"{joint}.rotate")[0]
                cmds.delete(aim)
                cmds.setAttr(f"{joint}.jointOrient", orientation[0], orientation[1], orientation[2])
                cmds.setAttr(f"{joint}.rotate", 0, 0, 0)
                cmds.parent(joint, parent)
                cmds.parent(children, joint)    
                """

            elif joint_info["orientation"] == "-x to child, +y to world +z": # right_arm_up
                cmds.parent(children, world=True)
                cmds.parent(joint, world=True)
                cmds.setAttr(f"{joint}.jointOrient", 0, 0, 0)                        
                aim = cmds.aimConstraint(main_child, joint, aimVector=[-1, 0, 0], upVector=[0, 1, 0], worldUpType="vector", worldUpVector=[0, 0, 1])[0]
                orientation = cmds.getAttr(f"{joint}.rotate")[0]
                cmds.delete(aim)
                cmds.setAttr(f"{joint}.jointOrient", orientation[0], orientation[1], orientation[2])
                cmds.setAttr(f"{joint}.rotate", 0, 0, 0)
                cmds.parent(joint, parent)
                cmds.parent(children, joint)   
            
            elif joint_info["orientation"] == "-x to child, +z to parent^child RH": # right_arm_down
                cmds.parent(children, world=True)
                cmds.parent(joint, world=True)
                cmds.setAttr(f"{joint}.jointOrient", 0, 0, 0) 
                v1 = om2.MVector(om2.MVector(cmds.xform(parent, query=True, t=True, ws=True)) - om2.MVector(cmds.xform(joint, query=True, t=True, ws=True)))
                v2 = om2.MVector(om2.MVector(cmds.xform(main_child, query=True, t=True, ws=True)) - om2.MVector(cmds.xform(joint, query=True, t=True, ws=True)))
                aux = v1 ^ v2
                aim = cmds.aimConstraint(main_child, joint, aimVector=[-1, 0, 0], upVector=[0, 0, 1], worldUpType="vector", worldUpVector=aux)[0]
                orientation = cmds.getAttr(f"{joint}.rotate")[0]
                cmds.delete(aim)
                cmds.setAttr(f"{joint}.jointOrient", orientation[0], orientation[1], orientation[2])
                cmds.setAttr(f"{joint}.rotate", 0, 0, 0)
                cmds.parent(joint, parent)
                cmds.parent(children, joint)   

            elif joint_info["orientation"] == "0, 0, keep": # finger tips
                if children: cmds.parent(children, world=True)
                cmds.setAttr(f"{joint}.jointOrientX", 0)
                cmds.setAttr(f"{joint}.jointOrientY", 0)
                if children: cmds.parent(children, joint)

            elif joint_info["orientation"] == "keep, copy, copy": # feet
                source_joint_orientation = cmds.getAttr(f"{source_joint}.jointOrient")[0]
                if children: cmds.parent(children, world=True)
                cmds.setAttr(f"{joint}.jointOrientY", source_joint_orientation[1])
                cmds.setAttr(f"{joint}.jointOrientZ", source_joint_orientation[2])
                if children: cmds.parent(children, joint)

            dag_iterator.next()
    
    def compute_total_error(self, joints, points):
        """
        Compute the total squared Euclidean distance between joints and their target points.
        
        Args:
            joints (list): List of joint names.
            points (list): List of point names.
        
        Returns:
            float: Sum of squared distances.
        """
        total_error = 0.0
        for jnt, pnt in zip(joints, points):
            joint_pos = om2.MVector(cmds.xform(jnt, query=True, translation=True, worldSpace=True))
            point_pos = om2.MVector(cmds.xform(pnt, query=True, translation=True, worldSpace=True))
            distance = (joint_pos - point_pos).length()
            total_error += distance * distance
        return total_error

    def align_joints_to_points_with_tolerance(self, joints, points, iterations=50, step_size=1.0, tolerance=1.0, max_iterations=1000):
        """
        Aligns a chain of joints to corresponding points in Maya with error tolerance.
        
        Args:
            joints (list): List of joint names ["pelvis", "spine_01", ..., "head"]
            points (list): List of point names ["point0", "point1", ..., "point8"]
            iterations (int): Number of iterations per batch.
            step_size (float): Step size for adjusting translations.
            tolerance (float): Maximum allowed deviation per joint (in translateY/Z for pelvis, translateX for others).
            max_iterations (int): Maximum total iterations.
        """
        if len(joints) != len(points):
            raise ValueError("Joints and points lists must have the same length.")
        
        # Ensure all joints and points exist
        for jnt, pnt in zip(joints, points):
            if not cmds.objExists(jnt):
                raise ValueError(f"Joint {jnt} does not exist.")
            if not cmds.objExists(pnt):
                raise ValueError(f"Point {pnt} does not exist.")
        
        # Initialize error tracking
        previous_error = self.compute_total_error(joints, points)
        total_iterations = 0
        
        while total_iterations < max_iterations:
            # Store initial translations to constrain deviations for this batch
            initial_translations = []
            for jnt in joints:
                tx = cmds.getAttr(f"{jnt}.translateX")
                ty = cmds.getAttr(f"{jnt}.translateY")
                tz = cmds.getAttr(f"{jnt}.translateZ")
                initial_translations.append((tx, ty, tz))
            
            # Run a batch of iterations
            for _ in range(iterations):
                for i, (jnt, pnt) in enumerate(zip(joints, points)):
                    # Get target point position in world space
                    target_pos = om2.MVector(cmds.xform(pnt, query=True, translation=True, worldSpace=True))
                    
                    # Get current joint position
                    joint_pos = om2.MVector(cmds.xform(jnt, query=True, translation=True, worldSpace=True))
                    
                    # Get allowed axes for movement
                    if i == 0:
                        # pelvis moves in Y and Z (world space)
                        world_y_axis = om2.MVector(0, 1, 0)
                        world_z_axis = om2.MVector(0, 0, 1)
                    else:
                        # Other joints move in parent's local X-axis
                        parent_joint = joints[i-1]
                        parent_matrix = om2.MMatrix(cmds.xform(parent_joint, query=True, matrix=True, worldSpace=True))
                        parent_transform = om2.MTransformationMatrix(parent_matrix)
                        local_x_axis = om2.MVector(1, 0, 0)
                        world_x_axis = local_x_axis * parent_transform.asMatrix()
                        world_x_axis.normalize()
                    
                    # Compute direction to target
                    direction = target_pos - joint_pos
                    
                    # Project direction onto allowed axes and compute adjustments
                    if i == 0:
                        # pelvis adjusts translateY and translateZ
                        delta_ty = direction * world_y_axis * step_size
                        delta_tz = direction * world_z_axis * step_size
                        delta_tx = 0.0  # translateX must remain 0
                    else:
                        # Other joints adjust translateX
                        delta_tx = direction * world_x_axis * step_size
                        delta_ty = 0.0
                        delta_tz = 0.0
                    
                    # Get current translations
                    current_tx = cmds.getAttr(f"{jnt}.translateX")
                    current_ty = cmds.getAttr(f"{jnt}.translateY")
                    current_tz = cmds.getAttr(f"{jnt}.translateZ")
                    initial_tx, initial_ty, initial_tz = initial_translations[i]
                    
                    # Compute new translations
                    new_tx = current_tx + delta_tx
                    new_ty = current_ty + delta_ty
                    new_tz = current_tz + delta_tz
                    
                    # Apply tolerance constraint
                    if i == 0:
                        # For pelvis, constrain translateY and translateZ
                        if abs(new_ty - initial_ty) > tolerance:
                            new_ty = initial_ty + tolerance if new_ty > initial_ty else initial_ty - tolerance
                        if abs(new_tz - initial_tz) > tolerance:
                            new_tz = initial_tz + tolerance if new_tz > initial_tz else initial_tz - tolerance
                        new_tx = 0.0  # Enforce translateX = 0
                    else:
                        # For other joints, constrain translateX
                        if abs(new_tx - initial_tx) > tolerance:
                            new_tx = initial_tx + tolerance if new_tx > initial_tx else initial_tx - tolerance
                        new_ty = 0.0
                        new_tz = 0.0
                    
                    # Apply translations
                    cmds.setAttr(f"{jnt}.translateX", new_tx)
                    cmds.setAttr(f"{jnt}.translateY", new_ty)
                    cmds.setAttr(f"{jnt}.translateZ", new_tz)
                    
                    # Ensure rotations are constrained
                    cmds.setAttr(f"{jnt}.rotateX", 0.0)
                    cmds.setAttr(f"{jnt}.rotateY", 0.0)
                
                total_iterations += 1
                if total_iterations >= max_iterations:
                    break
            
            # Check convergence
            current_error = self.compute_total_error(joints, points)
            improvement = (previous_error - current_error) / previous_error if previous_error > 0 else 0
            print(f"Batch {total_iterations // iterations}: Total squared error = {current_error:.6f}, Improvement = {improvement*100:.2f}%")
            if improvement < 0.01:  # Less than 1% improvement
                print("Converged: Improvement less than 1%.")
                break
            previous_error = current_error
        
        # Final error report
        final_error = self.compute_total_error(joints, points)
        print(f"Final total squared error: {final_error:.6f} after {total_iterations} iterations")
    
    def create_new_skeleton(self, old_skeleton_root):

        # Set namespace
        old_namespace = old_skeleton_root.split(":")[0]
        new_namespace = old_namespace.replace("old", "new")
        cmds.namespace(set=new_namespace)

        # Set joints_info
        body_joints_file = os.path.dirname(__file__) + "/resources/body_joints.json"
        body_joints_info = json.load(open(body_joints_file, "r"))
        head_joints_file = os.path.dirname(__file__) + "/resources/head_joints.json"
        head_joints_info = json.load(open(head_joints_file, "r"))
        if new_namespace == "new_body": joints_info = body_joints_info
        else: joints_info = head_joints_info

        # Get all possible vertex iterators
        old_combined_dagpath = om2.MSelectionList().add("old:combined").getDagPath(0)
        new_combined_dagpath = om2.MSelectionList().add("new:combined").getDagPath(0)
        old_head_dagpath = om2.MSelectionList().add("old_head:head_lod0_mesh").getDagPath(0)
        new_head_dagpath = om2.MSelectionList().add("new_head:head_lod0_mesh").getDagPath(0)
        old_teeth_dagpath = om2.MSelectionList().add("old_head:teeth_lod0_mesh").getDagPath(0)
        new_teeth_dagpath = om2.MSelectionList().add("new_head:teeth_lod0_mesh").getDagPath(0)
        old_eyeLeft_dagpath = om2.MSelectionList().add("old_head:eyeLeft_lod0_mesh").getDagPath(0)
        new_eyeLeft_dagpath = om2.MSelectionList().add("new_head:eyeLeft_lod0_mesh").getDagPath(0)
        old_eyeRight_dagpath = om2.MSelectionList().add("old_head:eyeRight_lod0_mesh").getDagPath(0)
        new_eyeRight_dagpath = om2.MSelectionList().add("new_head:eyeRight_lod0_mesh").getDagPath(0)
        vertex_iterators = {}
        vertex_iterators["old_combined"] = om2.MItMeshVertex(old_combined_dagpath)
        vertex_iterators["new_combined"] = om2.MItMeshVertex(new_combined_dagpath)
        vertex_iterators["old_head"] = om2.MItMeshVertex(old_head_dagpath)
        vertex_iterators["new_head"] = om2.MItMeshVertex(new_head_dagpath)
        vertex_iterators["old_teeth"] = om2.MItMeshVertex(old_teeth_dagpath)
        vertex_iterators["new_teeth"] = om2.MItMeshVertex(new_teeth_dagpath)
        vertex_iterators["old_eyeLeft"] = om2.MItMeshVertex(old_eyeLeft_dagpath)
        vertex_iterators["new_eyeLeft"] = om2.MItMeshVertex(new_eyeLeft_dagpath)
        vertex_iterators["old_eyeRight"] = om2.MItMeshVertex(old_eyeRight_dagpath)
        vertex_iterators["new_eyeRight"] = om2.MItMeshVertex(new_eyeRight_dagpath)

        # Create a DAG iterator starting from the given object
        source_root_dag_path = om2.MSelectionList().add(old_skeleton_root).getDagPath(0)
        dag_iterator = om2.MItDag(om2.MItDag.kDepthFirst, om2.MFn.kInvalid)
        dag_iterator.reset(source_root_dag_path, om2.MItDag.kDepthFirst, om2.MFn.kInvalid)
        
        while not dag_iterator.isDone():
            # Exclude non joints
            if dag_iterator.currentItem().apiType() != 121:
                dag_iterator.next()
                continue

            # Get source joint name
            source_joint_name = dag_iterator.partialPathName()
            source_joint_dag_path = om2.MSelectionList().add(source_joint_name).getDagPath(0)
            reference_joint_name = om2.MNamespace.stripNamespaceFromName(source_joint_name)

            # Set vertex iterators
            source_vertex_iterator = vertex_iterators[f"old_{joints_info[reference_joint_name]['reference_mesh']}"]
            target_vertex_iterator = vertex_iterators[f"new_{joints_info[reference_joint_name]['reference_mesh']}"]
                            
            # Create joint
            cmds.select(cl = True)
            target_joint_name = cmds.joint(p = (0, 0, 0), n = reference_joint_name)
            target_joint_dag_path = om2.MSelectionList().add(target_joint_name).getDagPath(0)
            
            # Match joint
            cull_distance_multiplier = 1.5
            valid_vertex_ids = [i for i in range(54412)]
            self.match_joint(joints_info, source_vertex_iterator, target_vertex_iterator, source_joint_dag_path, target_joint_dag_path)
            
            # Parent 
            old_parent = cmds.listRelatives(source_joint_name, parent=True)
            if old_parent:
                new_parent = old_parent[0].replace(old_namespace, new_namespace)
                cmds.parent(target_joint_dag_path, new_parent, a = True)
            
            dag_iterator.next()

        # Fix skeleton
        if new_namespace == "new_body":
            self.fix_body_skeleton(f"{new_namespace}:", f"{old_namespace}:")                

            """
            """
            # Fix spine
            if not cmds.namespace(exists=":temp"): cmds.namespace(add=":temp")
            cmds.namespace(set=":temp")
            cmds.duplicate(f"{old_namespace}:root")
            cmds.setAttr("temp:root.v", True)
            delete_joints = ["temp:clavicle_l", "temp:clavicle_r", "temp:spine_04_latissimus_l", "temp:clavicle_pec_l", "temp:spine_04_latissimus_r", "temp:clavicle_pec_r", "temp:thigh_l", "temp:thigh_r"]
            cmds.delete(delete_joints)
            joints = ["temp:pelvis", "temp:spine_01", "temp:spine_02", "temp:spine_03", "temp:spine_04", "temp:spine_05", "temp:neck_01", "temp:neck_02", "temp:head"]
            targets = [f"{new_namespace}:pelvis", f"{new_namespace}:spine_01", f"{new_namespace}:spine_02", f"{new_namespace}:spine_03", f"{new_namespace}:spine_04", f"{new_namespace}:spine_05", f"{new_namespace}:neck_01", f"{new_namespace}:neck_02", f"{new_namespace}:head"]
            self.align_joints_to_points_with_tolerance(joints, targets, iterations=50, step_size=0.1, tolerance=10.0, max_iterations=1000)
            spine_05_joints = [f"{new_namespace}:clavicle_l", f"{new_namespace}:clavicle_r", f"{new_namespace}:spine_04_latissimus_l", f"{new_namespace}:clavicle_pec_l", f"{new_namespace}:spine_04_latissimus_r", f"{new_namespace}:clavicle_pec_r"]
            pelvis_joints = [f"{new_namespace}:thigh_l", f"{new_namespace}:thigh_r"]
            cmds.parent(spine_05_joints, world=True)
            cmds.parent(pelvis_joints, world=True)
            cmds.delete(f"{new_namespace}:root")
            cmds.namespace(set=f":{new_namespace}")
            for item in cmds.ls("temp:*"): cmds.rename(item, om2.MNamespace.stripNamespaceFromName(item))
            cmds.parent(spine_05_joints, f"{new_namespace}:spine_05")
            cmds.parent(pelvis_joints, f"{new_namespace}:pelvis")      
    
        if new_namespace == "new_head":
            self.fix_head_skeleton(joints_info)

        cmds.namespace(set=":")
    
    def get_mesh_vertex_positions_from_scene(self, meshName):
        try:
            dagpath = om2.MSelectionList().add(meshName).getDagPath(0)

            mf_mesh = om2.MFnMesh(dagpath)
            positions = om2.MPointArray()

            positions = mf_mesh.getPoints()

            print(f"get_mesh_vertex_positions_from_scene was succesful for {meshName}")
            return [
                [positions[i].x, positions[i].y, positions[i].z]
                for i in range(len(positions))
            ]
        except RuntimeError:
            print(f"get_mesh_vertex_positions_from_scene ***FAILED*** for {meshName}")
            return []

    def run_vertices_command(self, calibrated, old_vertex_positions, new_vertex_positions, mesh_id):
        # Making deltas between old vertices positions and new one
        deltas = []
        i = 0
        for new_vertex, old_vertex in zip(new_vertex_positions, old_vertex_positions):
            delta = []
            for new, old in zip(new_vertex, old_vertex):
                delta.append(new - old)
            deltas.append(delta)
            #print(f"vertex {i}: {delta}")
            #i += 1

        # Commands to run
        new_neutral_mesh = SetVertexPositionsCommand(mesh_id, deltas, VectorOperation_Add)
        calculate_lower_LODs = CalculateMeshLowerLODsCommand(mesh_id)
        
        # Add nex vertex position deltas (NOT ABSOLUTE VALUES) onto existing vertex positions
        commands = CommandSequence()
        commands.add(new_neutral_mesh)
        #commands.add(calculate_lower_LODs)
        commands.run(calibrated)

        # Verify that everything went fine
        if not Status.isOk():
            status = Status.get()
            raise RuntimeError(f"Error run_vertices_command: {status.message}")

    def run_joints_command(self, reader, calibrated, namespace=""):
        # Making arrays for joints' transformations and their corresponding mapping arrays
        joint_translations = []
        joint_rotations = []


        for i in range(reader.getJointCount()):
            joint_name = reader.getJointName(i)
            if namespace != "": joint_name = namespace + ":" + joint_name

            translation = cmds.xform(joint_name, query=True, translation=True)
            joint_translations.append(translation)

            rotation = cmds.joint(joint_name, query=True, orientation=True)
            joint_rotations.append(rotation)

        # This is step 5 sub-step a
        set_new_joints_translations = SetNeutralJointTranslationsCommand(joint_translations)
        # This is step 5 sub-step b
        set_new_joints_rotations = SetNeutralJointRotationsCommand(joint_rotations)

        # Abstraction to collect all commands into a sequence, and run them with only one invocation
        commands = CommandSequence()
        # Add vertex position deltas (NOT ABSOLUTE VALUES) onto existing vertex positions
        commands.add(set_new_joints_translations)
        commands.add(set_new_joints_rotations)

        commands.run(calibrated)
        # Verify that everything went fine
        if not Status.isOk():
            status = Status.get()
            raise RuntimeError(f"Error run_joints_command: {status.message}")
        
    def save_body_dna(self):
        head_input_stream = FileStream(self.input_head_dna, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
        body_input_stream = FileStream(self.input_body_dna, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
        head_reader = BinaryStreamReader(head_input_stream, DataLayer_All)
        body_reader = BinaryStreamReader(body_input_stream, DataLayer_All)
        head_reader.read()
        body_reader.read()

        for reader in [head_reader, body_reader]:
            dnacalib_reader = DNACalibDNAReader(reader)
            
            """
            """
            # Modify meshes
            DNA_object = DNA(None, reader)
            mesh_elements = DNA_object.get_meshes()
            for mesh_element in mesh_elements:
                basename = mesh_element.name
                index = mesh_element.index
                if reader == head_reader: 
                    old_name = "old_head:" + basename
                    new_name = "new_head:" + basename
                    new_namespace = "new_head"
                else: 
                    old_name = "old_body:" + basename
                    new_name = "new_body:" + basename
                    new_namespace = "new_body"
                if cmds.objExists(new_name):
                    old_vertex_positions = self.get_mesh_vertex_positions_from_scene(old_name)
                    new_vertex_positions = self.get_mesh_vertex_positions_from_scene(new_name)
                    self.run_vertices_command(dnacalib_reader, old_vertex_positions, new_vertex_positions, index)
            
            # Modify skeleton
            if reader == head_reader: new_namespace = "new_head"
            else: new_namespace = "new_body"
            self.run_joints_command(reader, dnacalib_reader, new_namespace)
            
            # Save dna
            new_dna_folder = f"{self.input_metahuman_folder}/new_dna"
            if not os.path.exists(new_dna_folder): os.makedirs(new_dna_folder)
            if reader == head_reader: output_dna_file = new_dna_folder + "/new_head.dna"
            if reader == body_reader: output_dna_file = new_dna_folder + "/new_body.dna"
            output_stream = FileStream(output_dna_file, AccessMode_Write, OpenMode_Binary)
            writer = BinaryStreamWriter(output_stream)
            writer.setFrom(dnacalib_reader)
            writer.write()

        
        
        return
    
    def fix_pose(self):
        """
        """
        head_input_stream = FileStream(self.input_head_dna, AccessMode_Read, OpenMode_Binary)
        body_input_stream = FileStream(self.input_body_dna, AccessMode_Read, OpenMode_Binary)
        head_reader = BinaryStreamReader(head_input_stream, DataLayer_All)
        body_reader = BinaryStreamReader(body_input_stream, DataLayer_All)
        head_reader.read()
        body_reader.read()

        # Delete combined meshes
        #cmds.delete(["old:combined", "new:combined"])
        cmds.setAttr("old:combined.v", False)
        cmds.setAttr("new:combined.v", False)

        # Create skinweights for new meshes from dna skinweights
        for reader in [head_reader, body_reader]:
            
            # Put new items in ":" namespace
            if reader == head_reader: 
                dna_file = self.input_head_dna
                new_namespace = "new_head"
            else: 
                dna_file = self.input_body_dna
                new_namespace = "new_body"
            new_items = cmds.ls(f"{new_namespace}:*", type="transform")
            for i, item in enumerate(new_items): 
                cmds.rename(item, item.replace(new_namespace, ""))
                new_items[i] = item.replace(new_namespace, "")
            
            # Create skinweights
            dna_object = DNA(dna_file, reader)
            form = ProcessForm()
            maya_config = MayaConfig()
            lod0_mesh_elements = []
            for element in dna_object.get_meshes():
                if element.lod == 0: lod0_mesh_elements.append(element)
            maya_skinweights_handler = MayaSkinWeightsHandler(dna_object, form, maya_config)
            maya_skinweights_handler.create_skin_weights(lod0_mesh_elements)

            ## Create body rig logic
            #if reader == body_reader:
            #    return 
            #    rig_handler = MayaRigHandler(dna_object, form, maya_config)
            #    rig_handler.create_rig_logic()        
            
            # Put dna items back in its namespace
            for item in new_items: 
                cmds.rename(item, f"{new_namespace}:{item}")
        
        cmds.polyCube(n="starting_foot_l")
        cmds.DeleteHistory()
        aux = cmds.orientConstraint("new_body:foot_l", "starting_foot_l", offset=(0, 0, 0), weight=1)[0]
        cmds.delete(aux)
        cmds.polyCube(n="starting_foot_r")
        cmds.DeleteHistory()
        aux = cmds.orientConstraint("new_body:foot_r", "starting_foot_r", offset=(0, 0, 0), weight=1)[0]
        cmds.delete(aux)
        
        #cmds.file("F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp.mb", open=True, force=True)
        # Copy joint orientations from old to new body joints
        new_root_dagpath = om2.MSelectionList().add("new_body:root").getDagPath(0)
        dag_iterator = om2.MItDag().reset(new_root_dagpath)
        while not dag_iterator.isDone():
            new_joint = dag_iterator.partialPathName()
            old_joint = new_joint.replace("new_", "old_")
            old_orient = cmds.getAttr(f"{old_joint}.jointOrient")[0]
            cmds.setAttr(f"{new_joint}.jointOrient", old_orient[0], old_orient[1], old_orient[2])
            dag_iterator.next()

        # Match new head joints to new body joints
        dagpath = om2.MSelectionList().add("new_head:spine_04").getDagPath(0)
        dag_iterator = om2.MItDag().reset(dagpath)
        cmds.parent("new_body:spine_04", w=True)
        while not dag_iterator.isDone():
            head_joint = dag_iterator.partialPathName()
            body_joint = head_joint.replace("new_head", "new_body")
            if cmds.objExists(body_joint):
                body_joint_position = cmds.xform(body_joint, q=True, t=True, ws=True)
                body_joint_orientation = cmds.getAttr(f"{body_joint}.jointOrient")[0]
                cmds.xform(head_joint, t=body_joint_position, ws=True)
                cmds.setAttr(f"{head_joint}.jointOrient", body_joint_orientation[0], body_joint_orientation[1], body_joint_orientation[2])
            dag_iterator.next()
        cmds.parent("new_body:spine_04", "new_body:spine_03")

        # Make feet flat
        cmds.polyCube(n="posed_foot_l")
        cmds.DeleteHistory()
        aux = cmds.orientConstraint("new_body:foot_l", "posed_foot_l", offset=(0, 0, 0), weight=1)[0]
        cmds.delete(aux)
        cmds.polyCube(n="posed_foot_r")
        cmds.DeleteHistory()
        aux = cmds.orientConstraint("new_body:foot_r", "posed_foot_r", offset=(0, 0, 0), weight=1)[0]
        cmds.delete(aux)
        #
        aux = cmds.orientConstraint("starting_foot_l", "new_body:foot_l", offset=(0, 0, 0), weight=1)[0]
        cmds.delete(aux)
        aux = cmds.orientConstraint("starting_foot_r", "new_body:foot_r", offset=(0, 0, 0), weight=1)[0]
        cmds.delete(aux)
        #
        aux = cmds.orientConstraint("posed_foot_l", "new_body:foot_l", offset=(0, 0, 0), skip=["y", "z"], weight=1)[0]
        cmds.delete(aux)
        aux = cmds.orientConstraint("posed_foot_r", "new_body:foot_r", offset=(0, 0, 0), skip=["y", "z"], weight=1)[0]
        cmds.delete(aux)

        # Delete history for all meshes
        cmds.select(cmds.ls("new_head:*", et="transform"))
        cmds.select(cmds.ls("new_body:*", et="transform"), add=True)
        cmds.DeleteHistory()

        # Fix feet orientations
        for foot_joint in ["new_body:foot_l", "new_body:foot_r"]:
            old_foot_joint = foot_joint.replace("new_", "old_")
            foot_children = cmds.listRelatives(foot_joint, children=True)
            cmds.parent(foot_children, world=True)
            old_ori = cmds.getAttr(f"{old_foot_joint}.jointOrient")[0]
            cmds.setAttr(f"{foot_joint}.rotate", 0, 0, 0)
            cmds.setAttr(f"{foot_joint}.jointOrient", old_ori[0], old_ori[1], old_ori[2])
            cmds.parent(foot_children, foot_joint)
            #
            all_joints = cmds.listRelatives(foot_joint, ad=True)
            parents = {}
            for joint in all_joints:
                has_parent = cmds.listRelatives(joint, parent=True)
                if has_parent: 
                    parents[joint] = has_parent[0]
                    cmds.parent(joint, w=True)
                else: parents[joint] = None
            #
            for joint in all_joints:
                old_joint = joint.replace("new_", "old_")
                aux_joint = cmds.duplicate(old_joint)[0]
                cmds.parent(aux_joint, w=True)
                old_ori = cmds.getAttr(f"{aux_joint}.jointOrient")[0]
                cmds.delete(aux_joint)
                cmds.setAttr(f"{joint}.jointOrient", old_ori[0], old_ori[1], old_ori[2])
            #
            for joint in all_joints:            
                if parents[joint]: cmds.parent(joint, parents[joint])
        cmds.select(cl=True)

    def run(self):
        cmds.file(new=True, force=True)

        """
        """
        self.load_dna()
        #cmds.file(rename="F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp1_load_dna_done.mb")
        #cmds.file(f=True, save=True)
        
        #cmds.file("F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp1_load_dna_done.mb", open=True, force=True)
        self.load_new_meshes()
        #cmds.file(rename="F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp2_load_new_meshes_done.mb")
        #cmds.file(f=True, save=True)
        
        #cmds.file("F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp2_load_new_meshes_done.mb", open=True, force=True)
        self.create_new_skeleton("old_body:root")
        #cmds.file(rename="F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp3_create_body_skeleton_done.mb")
        #cmds.file(f=True, save=True)

        #cmds.file("F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp3_create_body_skeleton_done.mb", open=True, force=True)
        self.create_new_skeleton("old_head:spine_04")
        #cmds.file(rename="F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp4_create_head_skeleton_done.mb")
        #cmds.file(f=True, save=True)

        #cmds.file("F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp4_create_head_skeleton_done.mb", open=True, force=True)
        self.fix_pose()
        #cmds.file(rename="F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp5_fix_pose_done.mb")
        #cmds.file(f=True, save=True)
        
        #cmds.file("F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug/temp5_fix_pose_done.mb", open=True, force=True)
        self.save_body_dna()
        
        cmds.file(new=True, f=True)
        