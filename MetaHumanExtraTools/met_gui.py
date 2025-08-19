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
import logging

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
    from PySide6.QtCore import QSize, Qt, QMargins, Slot, Signal, QRect, QThread, QObject, QEvent # type: ignore
    from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QWizard, QFrame, QLabel, QLineEdit, QSpacerItem, QProgressBar # type: ignore
    from PySide6.QtGui import QIcon, QPalette, QMovie, QImage, QPixmap # type: ignore
except:
    from PySide2.QtCore import QSize, Qt, QMargins, Slot, Signal, QRect, QThread, QObject, QEvent
    from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QWizard, QFrame, QLabel, QLineEdit, QSpacerItem, QProgressBar
    from PySide2.QtGui import QIcon, QPalette, QMovie, QImage, QPixmap

    sys.modules["PySide6"] = __import__("PySide2")
    sys.modules["PySide6.QtCore"] = sys.modules["PySide2.QtCore"]
    sys.modules["PySide6.QtGui"] = sys.modules["PySide2.QtGui"]
    sys.modules["PySide6.QtWidgets"] = sys.modules["PySide2.QtWidgets"]

try: importlib.reload(ui_met_main_window)
except: import ui_met_main_window
try: importlib.reload(ui_met_joint_widget)
except: import ui_met_joint_widget

try: importlib.reload(met_main)
except: import met_main
try: importlib.reload(resources.data)
except: import resources.data

# Configure logging
for path in sys.path:
    if "MetaHumanExtraTools" in path: 
        met_path = path
        break
log_path = os.path.join(met_path, "met.log")
logger = logging.getLogger(__name__)
if logger.hasHandlers(): logger.handlers.clear()
handler = logging.FileHandler(log_path)
formatter = logging.Formatter("%(name)s|%(asctime)s|%(levelname)s|: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.setLevel(logging.DEBUG)
logger.info(f"starting met_gui logger")
logger.info("import met_gui")

class METJointWidget(QWidget, ui_met_joint_widget.Ui_METJointWidget):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setupUi(self)
        self.main_window = main_window        

class METMainWindow(QMainWindow, ui_met_main_window.Ui_METMainWindow):   

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode
        if self.is_metatahuman_customize_already_visible(): return
        self.maya_widget = self.get_maya_widget()        
        super().__init__(self.maya_widget)
        self.setupUi(self)

        # Maya version
        maya_version = float(cmds.about(iv=True).split(" ")[-1])
        if maya_version < 2023.3:
            self.modes_frame.hide()
            self.running_frame.hide()
            self.new_version_frame.hide()
            self.debug_frame.hide()
            self.obj_to_metahuman_button.setEnabled(False)
            self.metahuman_to_obj_button.setEnabled(False)
            self.resize(self.sizeHint())
            self.show()
            logger.info("MET window opened")
            return
        
        # Version
        self.new_version_frame.hide()
        self.update_progress_bar.hide()
        self.updated_successfully_label.hide()
        self.restart_met_button.hide()
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
        
        if not debug_mode: 
            self.debug_frame.hide()
            self.store_fix_axes_button.hide()
        self.maya_version_frame.hide()
        self.modes_frame.hide()
        self.running_frame.hide()
        self.done_label.hide()
        self.go_to_metahuman_folder_button.hide()
        self.metahuman_to_obj_info_frame.hide()
        self.obj_to_metahuman_info_frame.hide()
        self.fixable_joints_frame.hide()
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
        self.select_reference_vertices_button.clicked.connect(self.select_reference_vertices)
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
        self.restart_met_button.clicked.connect(self.restart_met)
        self.edit_fixable_joints_button.clicked.connect(self.show_fixable_joints_frame)
        self.store_fix_axes_button.clicked.connect(self.store_fix_axes)

        # Add fixable joint widgets
        body_joints_file = os.path.dirname(__file__) + "/resources/body_joints.json"
        self.body_joints_info = json.load(open(body_joints_file, "r"))
        self.fixable_joint_widgets = []
        already_placed_joints = []
        for joint in self.body_joints_info:
            if joint not in already_placed_joints:
                if self.body_joints_info[joint]["fixable"]:
                    
                    joint_widget = METJointWidget(self.fixable_joints_scroll_area_widget)
                    joint_widget.fixable_joint_label.setText(joint)
                    joint_widget.fixable_joint_x_button.setChecked(self.body_joints_info[joint]["fix_axes"][0])
                    joint_widget.fixable_joint_y_button.setChecked(self.body_joints_info[joint]["fix_axes"][1])
                    joint_widget.fixable_joint_z_button.setChecked(self.body_joints_info[joint]["fix_axes"][2])
                    self.fixable_joints_layout.addWidget(joint_widget)
                    self.fixable_joint_widgets.append(joint_widget)
                    already_placed_joints.append(joint)
                    #print(f"added {joint}")

                    # Place mirror
                    if joint[-2:] == "_l": joint = joint.replace("_l", "_r")
                    elif joint[-2:] == "_r": joint = joint.replace("_r", "_l")
                    else: continue
                    joint_widget = METJointWidget(self.fixable_joints_scroll_area_widget)
                    joint_widget.fixable_joint_label.setText(joint)
                    joint_widget.fixable_joint_x_button.setChecked(self.body_joints_info[joint]["fix_axes"][0])
                    joint_widget.fixable_joint_y_button.setChecked(self.body_joints_info[joint]["fix_axes"][1])
                    joint_widget.fixable_joint_z_button.setChecked(self.body_joints_info[joint]["fix_axes"][2])
                    self.fixable_joints_layout.addWidget(joint_widget)
                    self.fixable_joint_widgets.append(joint_widget)
                    already_placed_joints.append(joint)
                    #print(f"added {joint}")
    
    def store_fix_axes(self):
        body_joints_info = self.read_joint_widgets()
        body_joints_info_file = "F:/WorkspaceDesktop/met/MetaHumanExtraTools/resources/body_joints.json"
        json.dump(body_joints_info, open(body_joints_info_file, "w"), indent=4)
    
    def show_fixable_joints_frame(self):
        self.fixable_joints_frame.show()
    
    def restart_met(self):
        self.close()
        import importlib
        try:
            importlib.reload(met_gui)
        except:
            import met_gui
        met_gui.METMainWindow(debug_mode=False)
    
    def joints_button_pressed(self):
        logger.info("joints_button_pressed()")
        if self.joints_button.isChecked() == False:
            self.skinweights_button.setChecked(False)
            self.riglogic_button.setChecked(False)

    def skinweights_button_pressed(self):
        logger.info("skinweights_button_pressed")
        if self.skinweights_button.isChecked():
            self.joints_button.setChecked(True)
        else:
            self.riglogic_button.setChecked(False)

    def riglogic_button_pressed(self):
        logger.info("riglogic_button_pressed()")
        if self.riglogic_button.isChecked():
            self.joints_button.setChecked(True)
            self.skinweights_button.setChecked(True)
    
    def symmetrize_pressed(self):
        logger.info("symmetrize_pressed()")
        self.symmetrize_button.setChecked(True)
        self.original_button.setChecked(False)

    def keep_original_pressed(self):
        logger.info("keep_original_pressed()")
        self.original_button.setChecked(True)
        self.symmetrize_button.setChecked(False)
    
    def is_metatahuman_customize_already_visible(self):
        logger.info("is_metahuman_customize_already_visible()")
        local_version_dict = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "version.json"), "r"))
        title = f"Metahuman Extra Tools {local_version_dict['current_version']}"
        visible_mc_windows = []
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QWidget) and widget.windowTitle() == title:
                if widget.isVisible(): visible_mc_windows.append(widget)
                else: del widget
        
        return len(visible_mc_windows)
    
    def get_maya_widget(self) -> QWidget:
        logger.info("get_maya_widget()")
        for obj in QApplication.topLevelWidgets():
            if obj.objectName() == "MayaWindow":
                return obj
        raise RuntimeError("Could not find MayaWindow instance")
           
    def check_if_metahuman_to_obj_is_ready(self):
        logger.info("check_if_metahuman_to_obj_is_ready()")
        if self.metahuman_folder: self.metahuman_to_obj_run_button.setEnabled(True)
        else: self.metahuman_to_obj_run_button.setEnabled(False)

    def check_if_obj_to_metahuman_is_ready(self):
        logger.info("check_if_obj_to_metahuman_is_ready()")
        if self.metahuman_folder and self.combined and self.eyes and self.eyelashes and self.teeth: self.obj_to_metahuman_run_button.setEnabled(True)
        else: self.obj_to_metahuman_run_button.setEnabled(False)

    def select_metahuman_folder(self):
        logger.info("select_metahuman_folder()")
        metahuman_folder = None
        result = cmds.fileDialog2(fileMode=2, caption="Select MetaHuman folder:")
        if result: metahuman_folder = result[0]
        body_dna = f"{metahuman_folder}/body.dna"
        head_dna = f"{metahuman_folder}/head.dna"
        
        dna_files_ok = True
        for file in [body_dna, head_dna]:
            if not os.path.exists(file): dna_files_ok = False

        if metahuman_folder and dna_files_ok: 
            self.metahuman_folder = metahuman_folder
            self.metahuman_folder_button.setText(self.short_path(metahuman_folder, 48))
            self.metahuman_folder_button.setStyleSheet("font-size: 12px; color: white;")
            
        else: 
            self.metahuman_folder = None
            self.metahuman_folder_button.setText("MetaHuman folder")
            self.metahuman_folder_button.setStyleSheet("font-size: 16px; color: white;")
            
        self.check_if_metahuman_to_obj_is_ready()
        self.check_if_obj_to_metahuman_is_ready()      
    
    def download_file(self, file_url, local_path, max_retries=5):
        logger.info(f"download_file({file_url}, {local_path})")
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
                        logger.info(f"Downloaded {file_url} to {local_path}")
                        self.downloaded_file_count += 1
                        self.update_progress_bar.setValue(int(100 * self.downloaded_file_count / self.repo_file_count))
                        return True
                    else:
                        logger.warning(f"Failed to download {file_url}: HTTP {response.getcode()}")
                        return False
            except urllib.error.URLError as e:
                logger.info(f"Attempt {attempt + 1}/{max_retries} failed for {file_url}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s, 8s, 16s
                else:
                    logger.info(f"Failed to download {file_url} after {max_retries} attempts")
                    return False
            except OSError as e:
                logger.exception(f"Error saving {local_path}: {e}")
                return False
        return False

    def process_directory(self, api_url, temp_folder, repo_path=""):
        logger.info(f"process_directory(temp_folder={temp_folder})")
        """Recursively process repository contents and download files to temp folder."""
        downloaded_files = []  # Track successfully downloaded files
        try:
            # Fetch directory contents
            with urllib.request.urlopen(api_url, timeout=30) as response:
                if response.getcode() == 200:
                    items = json.loads(response.read().decode('utf-8'))
                    for i, item in enumerate(items):
                        item_name = item['name']
                        item_path = os.path.join(repo_path, item_name)
                        local_path = os.path.join(temp_folder, item_path.replace("/", os.sep))
                        
                        if item['type'] == 'file':
                            logger.info(f"Attempting to download {item_path}...")
                            if self.download_file(item['download_url'], local_path):
                                downloaded_files.append(local_path)
                            else:
                                return None  # Abort if any file fails
                        elif item['type'] == 'dir':
                            logger.info(f"Processing directory {item_path}...")
                            # Update subfolder API URL to use http
                            subfolder_url = item['url'].replace("https://api.github.com", "http://api.github.com")
                            subfolder_files = self.process_directory(subfolder_url, temp_folder, item_path)
                            if subfolder_files is None:
                                return None  # Abort if any subfolder file fails
                            downloaded_files.extend(subfolder_files)
                else:
                    logger.warning(f"Failed to fetch contents from {api_url}: HTTP {response.getcode()}")
                    return None
            return downloaded_files
        except urllib.error.URLError as e:
            logger.exception(f"Error fetching {api_url}: {e}")
            return None
        except OSError as e:
            logger.exception(f"Error accessing temp folder {local_path}: {e}")
            return None
    
    def count_files_in_repo(self, api_url):
        count = 0
        try:
            with urllib.request.urlopen(api_url, timeout=30) as response:
                if response.getcode() == 200:
                    items = json.loads(response.read().decode('utf-8'))
                    for item in items:
                        if item['type'] == 'file':
                            count += 1
                        elif item['type'] == 'dir':
                            subfolder_url = item['url'].replace("https://api.github.com", "http://api.github.com")
                            count += self.count_files_in_repo(subfolder_url)
                else:
                    logger.warning(f"Failed to fetch contents from {api_url}: HTTP {response.getcode()}")
        except Exception as e:
            logger.exception(f"Error counting files in {api_url}: {e}")
        return count
    
    def update(self):
        logger.info("update()")
        self.update_button.hide()
        self.update_progress_bar.show()
        self.resize(self.sizeHint())
        self.repaint()
        
        api_url = f"http://api.github.com/repos/virtual-pancakes/met/contents/?ref=main"
        self.repo_file_count = self.count_files_in_repo(api_url)
        if self.repo_file_count == 0: self.repo_file_count = 1
        self.downloaded_file_count = 0

        for path in sys.path:
            if "MetaHumanExtraTools" in path: 
                met_path = path
                break
        modules_folder = os.path.join(met_path, "..")
        #modules_folder = "E:/Downloads/modules"
        
        # Create a temporary directory for caching
        temp_folder = tempfile.mkdtemp()
        logger.info(f"Using temporary directory: {temp_folder}")

        # Process the repository and download files to temp folder
        logger.info(f"Starting download from {api_url}...")
        downloaded_files = self.process_directory(api_url, temp_folder)

        if downloaded_files is None:
            logger.info("Download failed; cleaning up temporary directory.")
            shutil.rmtree(temp_folder, ignore_errors=True)
            self.update_progress_bar.hide()
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
                logger.info(f"Moved {temp_path} to {final_path}")
            logger.info(f"All files successfully moved to {modules_folder}")
            self.update_progress_bar.hide()
            self.updated_successfully_label.show()
            #self.restart_met_button.show()
            self.resize(self.sizeHint())
        except OSError as e:
            logger.exception(f"Error moving files to {modules_folder}: {e}")
            self.update_progress_bar.hide()
            self.update_failed_frame.show()
            self.resize(self.sizeHint())
        finally:
            # Clean up temporary directory
            shutil.rmtree(temp_folder, ignore_errors=True)
            logger.info(f"Cleaned up temporary directory: {temp_folder}")
            self.resize(self.sizeHint())
        
    def short_path(self, path, max_length):
        logger.info(f"short_path({path}, {max_length})")
        if len(path) > max_length:
            return path[:3] + "..." + path[-(max_length - 6):]
        else:
            return path
    
    def show_metahuman_to_obj(self):
        logger.info("show_metahuman_to_obj")
        self.start_frame.hide()
        
        self.new_geometry_frame.hide()
        self.fix_pose_frame.hide()
        self.symmetrize_frame.show()
        self.metahuman_to_obj_run_button.show()
        self.obj_to_metahuman_run_button.hide()
        self.mode_label.setText("Metahuman to .OBJ")   

        self.modes_frame.show()
        self.adjustSize()
        self.resize(self.sizeHint())

    def show_obj_to_metahuman(self):
        logger.info("show_obj_to_metahuman")
        self.start_frame.hide()
        
        self.new_geometry_frame.show()
        self.fix_pose_frame.show()
        self.symmetrize_frame.hide()
        self.metahuman_to_obj_run_button.hide()
        self.obj_to_metahuman_run_button.show()
        self.mode_label.setText(".OBJ to Metahuman")

        self.modes_frame.show()
        self.adjustSize()
        self.resize(self.sizeHint())

    def back_to_start_frame(self):
        logger.info("back_to_start_frame()")
        self.metahuman_to_obj_run_button.setEnabled(False)
        self.metahuman_to_obj_run_button.setEnabled(False)
        self.metahuman_folder = None
        self.metahuman_folder_button.setText("MetaHuman folder")
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
        self.fixable_joints_frame.hide()
        self.start_frame.show()
        self.adjustSize()
        self.resize(self.sizeHint())
    
    def go_to_metahuman_folder(self):
        logger.info("go_to_metahuman_folder")
        os.startfile(self.metahuman_folder)
        #self.close()
    
    def combined_button_pressed(self):
        logger.info("combined_button_pressed()")
        result = cmds.fileDialog2(fileMode=1, caption="Select new combined .obj:")
        if result: 
            self.combined = result[0]
            self.combined_button.setText(self.short_path(self.combined, 48))
            self.combined_button.setStyleSheet("font-size: 10px")
        else:
            self.combined = None
            self.combined_button.setText("combined")
            self.combined_button.setStyleSheet("")
        self.check_if_obj_to_metahuman_is_ready()

    def eyes_button_pressed(self):
        logger.info("eyes_button_pressed()")
        result = cmds.fileDialog2(fileMode=1, caption="Select new eyes .obj:")
        if result: 
            self.eyes = result[0]
            self.eyes_button.setText(self.short_path(self.eyes, 48))
            self.eyes_button.setStyleSheet("font-size: 10px")
        else:
            self.eyes = None
            self.eyes_button.setText("eyes")
            self.eyes_button.setStyleSheet("")
        self.check_if_obj_to_metahuman_is_ready()

    def eyelashes_button_pressed(self):
        logger.info("eyelashes_button_pressed()")
        result = cmds.fileDialog2(fileMode=1, caption="Select new eyelashes .obj:")
        if result: 
            self.eyelashes = result[0]
            self.eyelashes_button.setText(self.short_path(self.eyelashes, 48))
            self.eyelashes_button.setStyleSheet("font-size: 10px")
        else:
            self.eyelashes = None
            self.eyelashes_button.setText("eyelashes")
            self.eyelashes_button.setStyleSheet("")
        self.check_if_obj_to_metahuman_is_ready()

    def teeth_button_pressed(self):
        logger.info("teeth_button_pressed()")
        result = cmds.fileDialog2(fileMode=1, caption="Select new teeth .obj:")
        if result: 
            self.teeth = result[0]
            self.teeth_button.setText(self.short_path(self.teeth, 48))
            self.teeth_button.setStyleSheet("font-size: 10px")
        else:
            self.teeth = None
            self.teeth_button.setText("teeth")
            self.teeth_button.setStyleSheet("")
        self.check_if_obj_to_metahuman_is_ready()
        
    def eyelashes_autogenerated_pressed(self):
        logger.info("eyelashes_autogenerated_pressed()")
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
        logger.info("teeth_autogenerated_pressed()")
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
        logger.info("press_metahuman_to_obj_run_button()")
        make_symmetric = self.symmetrize_button.isChecked()
        self.modes_frame.hide()
        self.metahuman_to_obj_info_frame.show()
        self.running_frame.show()
        self.resize(self.sizeHint())
        self.repaint()

        logger.info(f"met_main.MetahumanToObj({self.metahuman_folder}, {make_symmetric}).run()")
        try:
            result = met_main.MetahumanToObj(self, self.metahuman_folder, make_symmetric).run()
        except Exception as e:
            logger.exception(f"met_main.MetahumanToObj.run() failed: {e}")
            result = "Error. Share your /MetaHumanExtraTools/met.log on Discord for help."
        
        logger.info(f"met_main.MetahumanToObj.run() returned: {result}")
        if result == "Done!": 
            self.running_progress_bar.hide()
            self.done_label.show()
            self.go_to_metahuman_folder_button.show()
        else:
            self.running_progress_bar.setFormat(result)
            self.running_progress_bar.setStyleSheet("/*-----QProgressBar-----*/\nQProgressBar\n{\n   background-color: hsl(333, 100%, 50%);\n}\n\nQProgressBar:chunk\n{\n   background-color: hsl(333, 100%, 50%);\n}")
        self.resize(self.sizeHint())
                
    def press_obj_to_metahuman_run_button(self):
        logger.info("press_obj_to_metahuman_run_button()")
        self.modes_frame.hide()
        self.fixable_joints_frame.hide()
        self.obj_to_metahuman_info_frame.show()
        self.running_frame.show()
        self.resize(self.sizeHint())
        self.repaint()
        fix_pose = self.fix_pose_button.isChecked()
        custom_body_joints_info = self.read_joint_widgets()

        logger.info(f"met_main.ObjToMetahuman({self.combined}, {self.eyes}, {self.eyelashes}, {self.teeth}, {self.metahuman_folder}).run()")
        try:
            result = met_main.ObjToMetahuman(self, self.combined, self.eyes, self.eyelashes, self.teeth, self.metahuman_folder, fix_pose, custom_body_joints_info).run()
        except Exception as e:
            logger.exception(f"met_main.ObjToMetahuman.run() failed: {e}")
            result = "Error. Share your /MetaHumanExtraTools/met.log on Discord for help."
        
        logger.info(f"met_main.ObjToMetahuman.run() returned: {result}")
        if result == "Done!": 
            self.running_progress_bar.hide()
            self.done_label.show()
            self.go_to_metahuman_folder_button.show()
        else:
            self.running_progress_bar.hide()
            self.done_label.setText(result)
            self.done_label.setStyleSheet("color: hsl(333, 100%, 50%); font-weight: bold;")
            self.done_label.show()
            #self.running_progress_bar.setFormat(result)
            #self.running_progress_bar.setStyleSheet("/*-----QProgressBar-----*/\nQProgressBar\n{\n   background-color: hsl(333, 100%, 50%);\n}\n\nQProgressBar:chunk\n{\n   background-color: hsl(333, 100%, 50%);\n}")
        self.resize(self.sizeHint())
    
    def import_dna(self):
        logger.info("import_dna()")
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
            
    def select_reference_vertices(self):
        logger.info("select_reference_vertices()")
        joints_info_file = os.path.dirname(__file__) + "/resources/joints_info.json"
        joints_info = json.load(open(joints_info_file, "r"))
        selected_joint = om2.MNamespace.stripNamespaceFromName(cmds.ls(sl=True)[0])
        vertex_ids = joints_info[selected_joint]["reference_vertex_ids"]
        for id in vertex_ids:
            cmds.select(f"combined.vtx[{id}]", add=True)
        return

    def read_joint_widgets(self):
        custom_body_joints_info = self.body_joints_info.copy()
        for item in self.fixable_joint_widgets: 
            joint = item.fixable_joint_label.text()
            fix_axes = [item.fixable_joint_x_button.isChecked(), item.fixable_joint_y_button.isChecked(), item.fixable_joint_z_button.isChecked()]
            custom_body_joints_info[joint]["fix_axes"] = fix_axes

        return custom_body_joints_info
    
    def debug(self):
        """
        """
        logger.info("debug()")
        self.show_obj_to_metahuman()
        self.metahuman_folder = "F:/WorkspaceDesktop/met/MetaHumanExtraTools/private/debug"
        self.combined = f"{self.metahuman_folder}/new_OBJs/new_combined.obj"
        self.eyes = f"{self.metahuman_folder}/new_OBJs/new_eyes.obj"
        self.eyelashes = "auto generated"
        self.teeth = "auto generated"
        self.press_obj_to_metahuman_run_button()
