# Copyright Virtual Pancakes, 2025. All Rights Reserved.
import sys
import os
import importlib
import urllib.request
import shutil
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.mel as mel
import json
import time
import subprocess # type: ignore
import tempfile # type: ignore
import random # type: ignore

from dna import BinaryStreamReader, BinaryStreamWriter, DataLayer_All, FileStream, Status
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

# Use PySide6 for Maya 2025+ and PySide2 for Maya 2024-
try:
    from PySide6.QtCore import QSize, Qt, QMargins, Slot, Signal, QRect, QThread, QObject, QEvent
    from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QWizard, QFrame, QLabel, QLineEdit, QSpacerItem
    from PySide6.QtGui import QIcon, QPalette, QMovie, QImage, QPixmap
except:
    from PySide2.QtCore import QSize, Qt, QMargins, Slot, Signal, QRect, QThread, QObject, QEvent
    from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QWizard, QFrame, QLabel, QLineEdit, QSpacerItem
    from PySide2.QtGui import QIcon, QPalette, QMovie, QImage

    sys.modules["PySide6"] = __import__("PySide2")
    sys.modules["PySide6.QtCore"] = sys.modules["PySide2.QtCore"]
    sys.modules["PySide6.QtGui"] = sys.modules["PySide2.QtGui"]
    sys.modules["PySide6.QtWidgets"] = sys.modules["PySide2.QtWidgets"]

try: importlib.reload(ui_met_main_window)
except: import ui_met_main_window

try: importlib.reload(met_main)
except: import met_main
try: importlib.reload(resources.data)
except: import resources.data

class OriginalMetahuman:
    json_file = None
    asset_id = None
    mhc_version = None
    name = None
    preview_image = None
    small_preview_image = None
    source_files_path = None
    dna_file = None
    body_file = None
    gender = None
    height = None
    weight = None        

    def print_info(self):
        print(f"    json file:          {self.json_file}")
        print(f"    asset id:           {self.asset_id}")
        print(f"    mhc version:        {self.mhc_version}")
        print(f"    preview image:      {self.preview_image}")
        print(f"    small preview image:{self.small_preview_image}")
        print(f"    source files path:  {self.source_files_path}")
        print(f"    dna file:           {self.dna_file}")
        print(f"    body file:          {self.body_file}")
        print(f"    name:               {self.name}")
        print(f"    gender:             {self.gender}")
        print(f"    height:             {self.height}")
        print(f"    weight:             {self.weight}")
        print()

class METMainWindow(QMainWindow, ui_met_main_window.Ui_METMainWindow):   

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode
        if self.is_metatahuman_customize_already_visible(): return
        self.maya_widget = self.get_maya_widget()        
        super().__init__(self.maya_widget)
        self.setupUi(self)

        # Version
        self.new_version_frame.hide()
        self.update_completed_frame.hide()
        self.update_failed_frame.hide()
        self.artstation_link_label.setOpenExternalLinks(True)
        self.fab_link_label.setOpenExternalLinks(True)
        local_version_dict = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "version.json"), "r"))
        self.setWindowTitle(f"Metahuman Extra Tools {local_version_dict['current_version']}")
        if local_version_dict["checked_for_new_version"]:
            if local_version_dict["current_version"] != local_version_dict["newest_version"]: 
                self.changes_label.setText(local_version_dict["newest_version"] + "\n" + local_version_dict["newest_version_changes"])
                self.new_version_frame.show()
        else:
            self.update_failed_frame.show()
        
        # Set initial state
        self.metahuman_folder = None
        self.combined = None
        self.eyes = None
        self.eyelashes = "auto generated"
        self.teeth = "auto generated"
        
        if not debug_mode: self.debug_frame.hide()
        self.modes_frame.hide()
        self.running_frame.hide()
        self.go_to_metahuman_folder_button.hide()
        self.metahuman_to_obj_info_frame.hide()
        self.obj_to_metahuman_info_frame.hide()
        self.resize(self.sizeHint())
        self.show()
        #self.adjustSize()
        self.resize(self.sizeHint())

        # Set information images
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dna_options_body_image_path = os.path.join(script_dir, "resources", "dna_options_body.png")
        dna_options_head_image_path = os.path.join(script_dir, "resources", "dna_options_head.png")
        self.dna_options_body_label.setPixmap(QPixmap(dna_options_body_image_path))
        self.dna_options_head_label.setPixmap(QPixmap(dna_options_head_image_path))

        # Connect buttons
        self.metahuman_to_obj_button.clicked.connect(self.show_metahuman_to_obj)
        self.obj_to_metahuman_button.clicked.connect(self.show_obj_to_metahuman)
        self.update_button.clicked.connect(self.update)
        self.debug_button.clicked.connect(self.debug)
        self.metahuman_folder_button.clicked.connect(self.select_metahuman_folder)
        self.back_button.clicked.connect(self.back_to_start_frame)
        self.symmetrize_button.clicked.connect(self.symmetrize_pressed)
        self.original_button.clicked.connect(self.keep_original_pressed)
        self.metahuman_to_obj_run_button.clicked.connect(self.press_metahuman_to_obj_run_button)
        self.obj_to_metahuman_run_button.clicked.connect(self.press_obj_to_metahuman_run_button)
        self.import_dna_button.clicked.connect(self.import_dna)
        self.go_to_metahuman_folder_button.clicked.connect(self.go_to_metahuman_folder)
        self.combined_button.clicked.connect(self.combined_button_pressed)
        self.eyes_button.clicked.connect(self.eyes_button_pressed)
        self.eyelashes_button.clicked.connect(self.eyelashes_button_pressed)
        self.teeth_button.clicked.connect(self.teeth_button_pressed)
        self.eyelashes_autogenerated_button.clicked.connect(self.eyelashes_autogenerated_pressed)
        self.teeth_autogenerated_button.clicked.connect(self.teeth_autogenerated_pressed)
        self.joints_button.clicked.connect(self.joints_button_pressed)
        self.skinweights_button.clicked.connect(self.skinweights_button_pressed)
        self.riglogic_button.clicked.connect(self.riglogic_button_pressed)

    def joints_button_pressed(self):
        if self.joints_button.isChecked() == False:
            self.skinweights_button.setChecked(False)
            self.riglogic_button.setChecked(False)

    def skinweights_button_pressed(self):
        if self.skinweights_button.isChecked():
            self.joints_button.setChecked(True)
        else:
            self.riglogic_button.setChecked(False)

    def riglogic_button_pressed(self):
        if self.riglogic_button.isChecked():
            self.joints_button.setChecked(True)
            self.skinweights_button.setChecked(True)
    
    def symmetrize_pressed(self):
        self.symmetrize_button.setChecked(True)
        self.original_button.setChecked(False)

    def keep_original_pressed(self):
        self.original_button.setChecked(True)
        self.symmetrize_button.setChecked(False)
    
    def is_metatahuman_customize_already_visible(self):
        visible_mc_windows = []
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QWidget) and widget.windowTitle() == "Metahuman Extra Tools":
                if widget.isVisible(): visible_mc_windows.append(widget)
                else: del widget
        
        return len(visible_mc_windows)
    
    def get_maya_widget(self) -> QWidget:
        for obj in QApplication.topLevelWidgets():
            if obj.objectName() == "MayaWindow":
                return obj
        raise RuntimeError("Could not find MayaWindow instance")
           
    def check_if_metahuman_to_obj_is_ready(self):
        if self.metahuman_folder: self.metahuman_to_obj_run_button.setEnabled(True)
        else: self.metahuman_to_obj_run_button.setEnabled(False)

    def check_if_obj_to_metahuman_is_ready(self):
        if self.metahuman_folder and self.combined and self.eyes and self.eyelashes and self.teeth: self.obj_to_metahuman_run_button.setEnabled(True)
        else: self.obj_to_metahuman_run_button.setEnabled(False)

    def select_metahuman_folder(self):
        metahuman_folder = None
        result = cmds.fileDialog2(fileMode=2, caption="Select Metahuman folder:")
        if result: metahuman_folder = result[0]
        body_dna = f"{metahuman_folder}/body.dna"
        head_dna = f"{metahuman_folder}/head.dna"
        
        dna_files_ok = True
        for file in [body_dna, head_dna]:
            if not os.path.exists(file): dna_files_ok = False

        if metahuman_folder and dna_files_ok: 
            self.metahuman_folder = metahuman_folder
            self.metahuman_folder_button.setText(self.short_path(metahuman_folder, 50))
            self.metahuman_folder_button.setStyleSheet("font-size: 12px; color: white;")
            
        else: 
            self.metahuman_folder = None
            self.metahuman_folder_button.setText("Metahuman folder")
            self.metahuman_folder_button.setStyleSheet("font-size: 16px; color: white;")
            
        self.check_if_metahuman_to_obj_is_ready()
        self.check_if_obj_to_metahuman_is_ready()      
    
    def download_file(self, file_url, local_path, max_retries=5):
        """Download a single file to the specified path with retries."""
        # Convert https to http for raw file URLs
        file_url = file_url.replace("https://raw.githubusercontent.com", "http://raw.githubusercontent.com")
        for attempt in range(max_retries):
            try:
                # Create a request
                req = urllib.request.Request(file_url)
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.getcode() == 200:
                        # Ensure the parent directory exists
                        os.makedirs(os.path.dirname(local_path), exist_ok=True)
                        # Download in chunks
                        with open(local_path, 'wb') as f:
                            while True:
                                chunk = response.read(8192)  # Read 8KB at a time
                                if not chunk:
                                    break
                                f.write(chunk)
                        print(f"Downloaded {file_url} to {local_path}")
                        return True
                    else:
                        print(f"Failed to download {file_url}: HTTP {response.getcode()}")
                        return False
            except urllib.error.URLError as e:
                print(f"Attempt {attempt + 1}/{max_retries} failed for {file_url}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s, 8s, 16s
                else:
                    print(f"Failed to download {file_url} after {max_retries} attempts")
                    return False
            except OSError as e:
                print(f"Error saving {local_path}: {e}")
                return False
        return False

    def process_directory(self, api_url, temp_folder, repo_path=""):
        """Recursively process repository contents and download files to temp folder."""
        downloaded_files = []  # Track successfully downloaded files
        try:
            # Fetch directory contents
            with urllib.request.urlopen(api_url, timeout=30) as response:
                if response.getcode() == 200:
                    items = json.loads(response.read().decode('utf-8'))
                    for item in items:
                        item_name = item['name']
                        item_path = os.path.join(repo_path, item_name)
                        local_path = os.path.join(temp_folder, item_path.replace("/", os.sep))
                        
                        if item['type'] == 'file':
                            print(f"Attempting to download {item_path}...")
                            if self.download_file(item['download_url'], local_path):
                                downloaded_files.append(local_path)
                            else:
                                return None  # Abort if any file fails
                        elif item['type'] == 'dir':
                            print(f"Processing directory {item_path}...")
                            # Update subfolder API URL to use http
                            subfolder_url = item['url'].replace("https://api.github.com", "http://api.github.com")
                            subfolder_files = self.process_directory(subfolder_url, temp_folder, item_path)
                            if subfolder_files is None:
                                return None  # Abort if any subfolder file fails
                            downloaded_files.extend(subfolder_files)
                else:
                    print(f"Failed to fetch contents from {api_url}: HTTP {response.getcode()}")
                    return None
            return downloaded_files
        except urllib.error.URLError as e:
            print(f"Error fetching {api_url}: {e}")
            return None
        except OSError as e:
            print(f"Error accessing temp folder {local_path}: {e}")
            return None
    
    def update(self):
        api_url = f"http://api.github.com/repos/virtual-pancakes/met/contents/?ref=main"
        #modules_folder = "C:/modules"
        for path in sys.path:
            if "MetaHumanExtraTools" in path: 
                met_path = path
                break
        modules_folder = os.path.join(met_path, "..")
        
        # Create a temporary directory for caching
        temp_folder = tempfile.mkdtemp()
        print(f"Using temporary directory: {temp_folder}")

        # Process the repository and download files to temp folder
        print(f"Starting download from {api_url}...")
        downloaded_files = self.process_directory(api_url, temp_folder)

        if downloaded_files is None:
            print("Download failed; cleaning up temporary directory.")
            shutil.rmtree(temp_folder, ignore_errors=True)
            self.new_version_frame.hide()
            self.update_failed_frame.show()
            self.resize(self.sizeHint())
            return

        # All downloads succeeded; move files to final folder
        try:        
            os.makedirs(modules_folder, exist_ok=True)
            for temp_path in downloaded_files:
                if ".gitignore" in temp_path: continue
                if "README.txt" in temp_path: continue
                if "userSetup.py" in temp_path: continue
                relative_path = os.path.relpath(temp_path, temp_folder)
                final_path = os.path.join(modules_folder, relative_path)
                os.makedirs(os.path.dirname(final_path), exist_ok=True)
                shutil.move(temp_path, final_path)
                print(f"Moved {temp_path} to {final_path}")
            print(f"All files successfully moved to {modules_folder}")
            self.new_version_frame.hide()
            self.update_completed_frame.show()
        except OSError as e:
            print(f"Error moving files to {modules_folder}: {e}")
            self.new_version_frame.hide()
            self.update_failed_frame.show()
        finally:
            # Clean up temporary directory
            shutil.rmtree(temp_folder, ignore_errors=True)
            print(f"Cleaned up temporary directory: {temp_folder}")
            self.resize(self.sizeHint())
        
    def short_path(self, path, max_length):
        if len(path) > max_length:
            return path[:3] + "..." + path[-(max_length - 6):]
        else:
            return path
    
    def show_metahuman_to_obj(self):
        self.start_frame.hide()
        
        self.new_geometry_frame.hide()
        self.symmetrize_frame.show()
        self.metahuman_to_obj_run_button.show()
        self.obj_to_metahuman_run_button.hide()
        self.mode_label.setText("Metahuman to .OBJ")   

        self.modes_frame.show()
        self.adjustSize()
        self.resize(self.sizeHint())

    def show_obj_to_metahuman(self):
        self.start_frame.hide()
        
        self.new_geometry_frame.show()
        self.symmetrize_frame.hide()
        self.metahuman_to_obj_run_button.hide()
        self.obj_to_metahuman_run_button.show()
        self.mode_label.setText(".OBJ to Metahuman")

        self.modes_frame.show()
        self.adjustSize()
        self.resize(self.sizeHint())

    def back_to_start_frame(self):
        self.metahuman_to_obj_run_button.setEnabled(False)
        self.metahuman_to_obj_run_button.setEnabled(False)
        self.metahuman_folder = None
        self.metahuman_folder_button.setText("Metahuman folder")
        self.metahuman_folder_button.setStyleSheet("font-size: 16px; color: white;")
        self.combined = None
        self.combined_button.setText("combined")
        self.combined_button.setStyleSheet("")
        self.eyes = None
        self.eyes_button.setText("eyes")
        self.eyes_button.setStyleSheet("")
        self.eyelashes = None
        self.eyelashes_button.setText("eyelashes")
        self.eyelashes_button.setStyleSheet("")
        self.teeth = None
        self.teeth_button.setText("teeth")
        self.teeth_button.setStyleSheet("")
        self.eyelashes_autogenerated_button.setStyleSheet("font-size: 10px")
        self.eyelashes_autogenerated_button.setText("auto generated")
        self.eyelashes_button.setEnabled(False)
        self.eyelashes = "auto generated"
        self.teeth_autogenerated_button.setStyleSheet("font-size: 10px")
        self.teeth_autogenerated_button.setText("auto generated")
        self.teeth_button.setEnabled(False)
        self.teeth = "auto generated"
        self.modes_frame.hide()
        self.start_frame.show()
        self.adjustSize()
        self.resize(self.sizeHint())
    
    def go_to_metahuman_folder(self):
        os.startfile(self.metahuman_folder)
        #self.close()
    
    def combined_button_pressed(self):
        result = cmds.fileDialog2(fileMode=1, caption="Select new combined .obj:")
        if result: 
            self.combined = result[0]
            self.combined_button.setText(self.short_path(self.combined, 50))
            self.combined_button.setStyleSheet("font-size: 10px")
        else:
            self.combined = None
            self.combined_button.setText("combined")
            self.combined_button.setStyleSheet("")
        self.check_if_obj_to_metahuman_is_ready()

    def eyes_button_pressed(self):
        result = cmds.fileDialog2(fileMode=1, caption="Select new eyes .obj:")
        if result: 
            self.eyes = result[0]
            self.eyes_button.setText(self.short_path(self.eyes, 50))
            self.eyes_button.setStyleSheet("font-size: 10px")
        else:
            self.eyes = None
            self.eyes_button.setText("eyes")
            self.eyes_button.setStyleSheet("")
        self.check_if_obj_to_metahuman_is_ready()

    def eyelashes_button_pressed(self):
        result = cmds.fileDialog2(fileMode=1, caption="Select new eyelashes .obj:")
        if result: 
            self.eyelashes = result[0]
            self.eyelashes_button.setText(self.short_path(self.eyelashes, 50))
            self.eyelashes_button.setStyleSheet("font-size: 10px")
        else:
            self.eyelashes = None
            self.eyelashes_button.setText("eyelashes")
            self.eyelashes_button.setStyleSheet("")
        self.check_if_obj_to_metahuman_is_ready()

    def teeth_button_pressed(self):
        result = cmds.fileDialog2(fileMode=1, caption="Select new teeth .obj:")
        if result: 
            self.teeth = result[0]
            self.teeth_button.setText(self.short_path(self.teeth, 50))
            self.teeth_button.setStyleSheet("font-size: 10px")
        else:
            self.teeth = None
            self.teeth_button.setText("teeth")
            self.teeth_button.setStyleSheet("")
        self.check_if_obj_to_metahuman_is_ready()
        
    def eyelashes_autogenerated_pressed(self):
        if self.eyelashes_autogenerated_button.text() == "auto generated":
            self.eyelashes_autogenerated_button.setStyleSheet("")
            self.eyelashes_autogenerated_button.setText("OBJ")
            self.eyelashes_button.setEnabled(True)
            self.eyelashes = None
        else:
            self.eyelashes_autogenerated_button.setStyleSheet("font-size: 10px")
            self.eyelashes_autogenerated_button.setText("auto generated")
            self.eyelashes_button.setText("eyelashes")
            self.eyelashes_button.setStyleSheet("")
            self.eyelashes_button.setEnabled(False)
            self.eyelashes = "auto generated"
        self.check_if_obj_to_metahuman_is_ready()

    def teeth_autogenerated_pressed(self):
        if self.teeth_autogenerated_button.text() == "auto generated":
            self.teeth_autogenerated_button.setStyleSheet("")
            self.teeth_autogenerated_button.setText("OBJ")
            self.teeth_button.setEnabled(True)
            self.teeth = None
        else:
            self.teeth_autogenerated_button.setStyleSheet("font-size: 10px")
            self.teeth_autogenerated_button.setText("auto generated")
            self.teeth_button.setText("teeth")
            self.teeth_button.setStyleSheet("")
            self.teeth_button.setEnabled(False)
            self.teeth = "auto generated"
        self.check_if_obj_to_metahuman_is_ready()
    
    def press_metahuman_to_obj_run_button(self):
        make_symmetric = self.symmetrize_button.isChecked()
        self.modes_frame.hide()
        self.metahuman_to_obj_info_frame.show()
        self.running_frame.show()
        self.resize(self.sizeHint())

        result = met_main.MetahumanToObj(self.metahuman_folder, make_symmetric).run()
        
        self.running_label.setText(result)
        if result == "Done!": 
            self.running_label.setStyleSheet("color: hsl(177, 100%, 50%); font-weight: bold")
            self.go_to_metahuman_folder_button.show()
        else: self.running_label.setStyleSheet("color: hsl(333, 100%, 50%); font-weight: bold")
        self.resize(self.sizeHint())
                
    def press_obj_to_metahuman_run_button(self):
        self.modes_frame.hide()
        self.obj_to_metahuman_info_frame.show()
        self.running_frame.show()
        self.resize(self.sizeHint())

        result = met_main.ObjToMetahuman(self.combined, self.eyes, self.eyelashes, self.teeth, self.metahuman_folder).run()
        
        self.running_label.setText(result)
        if result == "Done!": 
            self.running_label.setStyleSheet("color: hsl(177, 100%, 50%); font-weight: bold")
            self.go_to_metahuman_folder_button.show()
        else: self.running_label.setStyleSheet("color: hsl(333, 100%, 50%); font-weight: bold")
        self.resize(self.sizeHint())
    
    def import_dna(self):
        #cmds.file(new=True, f=True)
        response = cmds.fileDialog2(fileMode=1, caption="Select DNA file:")
        if response: 
            # Create dna object
            dna_path = response[0]            
            print(f"loading dna: {dna_path}")        
            input_stream = FileStream(dna_path, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
            reader = BinaryStreamReader(input_stream, DataLayer_All)
            reader.read()
            dna_object = DNA(dna_path, reader)

            # Construct maya mesh handler
            form = ProcessForm()
            maya_config = MayaConfig()
            maya_mesh_handler = MayaMeshHandler(dna_object, form, maya_config)
            #mesh_element = dna_object.get_mesh(0)
            mesh_elements = dna_object.get_meshes()

            # Add meshes to scene
            dna_meshes = []
            for element in mesh_elements:
                if element.lod > -1:
                    maya_mesh_handler.add_mesh_to_scene(element)
                    maya_mesh_handler.add_mesh_uv(element)
                    maya_mesh_handler.add_mesh_shader(element)
                    dna_meshes.append(element.name)

            # Add joints
            if self.joints_button.isChecked():
                cmds.group(empty=True, name="head_grp") # Necessary group when creating meshes and joints from dna
                maya_joint_handler = MayaJointHandler(dna_object, form, maya_config)
                maya_joint_handler.create_joints()

            # Set skinweights
            if self.skinweights_button.isChecked():
                maya_skinweights_handler = MayaSkinWeightsHandler(dna_object, form, maya_config)
                for element in mesh_elements:
                    maya_skinweights_handler.create_skin_weights([element])

            # Create rig logic
            if self.riglogic_button.isChecked():
                rig_handler = MayaRigHandler(dna_object, form, maya_config)
                rig_handler.create_rig_logic()

            # Close window
            cmds.select(cl=True)
            self.close()
            
    def debug(self):
        self.show_obj_to_metahuman()
        self.metahuman_folder = "F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug"
        self.combined = f"{self.metahuman_folder}/new_OBJs/new_combined.obj"
        self.eyes = f"{self.metahuman_folder}/new_OBJs/new_eyes.obj"
        self.eyelashes = "auto generated"
        self.teeth = "auto generated"
        self.press_obj_to_metahuman_run_button()

        



