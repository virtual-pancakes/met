# Copyright Virtual Pancakes, 2025. All Rights Reserved.
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import pkg_resources
import subprocess
import json
import os
import sys

def initializePlugin(plugin):
    #om2.MFnPlugin(plugin)
    
    # Install requests module to be able to check for updates
    if "requests" not in [p.project_name for p in pkg_resources.working_set]:
        subprocess.run(["mayapy", "-m", "pip", "install", "requests"]) 
    
    # Check if new version available
    met_path = False
    for path in sys.path:
        if "MetaHumanExtraTools" in path: 
            met_path = path
            break
    import requests
    local_json_path = os.path.join(os.path.abspath(met_path), "version.json")
    live_json_link = "https://raw.githubusercontent.com/virtual-pancakes/met/refs/heads/main/MetaHumanExtraTools/version.json"
    local_dict = json.load(open(local_json_path, "r"))
    live_dict = requests.get(live_json_link).json()
    local_version = local_dict["current_version"]
    live_version = live_dict["current_version"]
    if local_version != live_version: 
        print("there is a new version available")
        local_dict["newest_version"] = live_version = live_dict["current_version"]
        local_dict["newest_changes"] = live_version = live_dict["current_changes"]
        json.dump(local_dict, open(local_json_path, "w"), indent=4)
    else:
        print("version up to date")
    
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