# Copyright Virtual Pancakes, 2025. All Rights Reserved.
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import pkg_resources
import subprocess

def initializePlugin(plugin):
    #om2.MFnPlugin(plugin)
    
    # Install requests module to be able to check for updates
    if "requests" not in [p.project_name for p in pkg_resources.working_set]:
        subprocess.run(["mayapy", "-m", "pip", "install", "requests"]) 
    
    # Load MetaHumanForMaya
    try:
        if not cmds.pluginInfo("MetaHumanForMaya.py", query=True, loaded=True): cmds.loadPlugin("MetaHumanForMaya.py")
    except:
        raise Exception("MetaHumanForMaya plugin not found")
    
    # Install into MetaHuman top menu
    metahuman_menu_items = cmds.menu("MetaHuman", query=True, itemArray=True)
    cmds.menuItem(label="Metahuman Extra Tools", command="import met_gui; met_gui.METMainWindow()", parent="MetaHuman", insertAfter=metahuman_menu_items[2])
    print("MetahumanExtraTools loaded")

# Uninitialize the plug-in
def uninitializePlugin(plugin):
    #om2.MFnPlugin(plugin)
    pass