# Copyright Virtual Pancakes, 2025. All Rights Reserved.
import maya.cmds as cmds
import maya.mel as mel
import os

def create_metahuman_extra_tools_shelf():
    shelf_name = "MetaHuman_Extra_Tools"
    icon_path = os.path.dirname(__file__) + "/resources/shelf_icon.png"
    command = """import met_gui
met_gui_object = met_gui.METMainWindow()
"""    
    # Add shelf if it doesn't already exist
    shelves_top_level = mel.eval("$aux = $gShelfTopLevel;")
    shelves = cmds.tabLayout(shelves_top_level, query=True, childArray=True)
    if shelf_name not in shelves: 
        mel.eval(f'addNewShelfTab "{shelf_name}";')

    #Add shelf button if it doesn't already exist
    if cmds.layout("MetaHuman_Extra_Tools", nch=True, query=True) == 0:
        cmds.shelfButton( label="Metahuman Extra Tools", command=command, parent="MetaHuman_Extra_Tools", image=icon_path)