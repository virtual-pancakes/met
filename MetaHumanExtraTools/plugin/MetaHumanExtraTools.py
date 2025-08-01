# Copyright Virtual Pancakes, 2025. All Rights Reserved.
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import pkg_resources
import subprocess
import json
import os
import sys
import urllib.request
import logging
from logging import Logger


def initializePlugin(plugin):
    #om2.MFnPlugin(plugin)

    # Get MetaHumanExtraTools path
    for path in sys.path:
        if "MetaHumanExtraTools" in path: 
            met_path = path
            break

    # Configure logging
    log_path = os.path.join(met_path, "met.log")
    open(log_path, "w").write("")
    logger = logging.getLogger(__name__)
    if logger.hasHandlers(): logger.handlers.clear()
    handler = logging.FileHandler(log_path)
    formatter = logging.Formatter("%(name)s|%(asctime)s|%(levelname)s|: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler) 
    logger.setLevel(logging.DEBUG)
    logger.info(f"starting initializePlugin logger ({logger})")
    logger.info(f"log_path: {log_path}")
    logger.info("Initializing MetaHumanExtraTools plugin")
        
    # Check if new version available
    local_json_path = os.path.join(os.path.abspath(met_path), "version.json")
    live_json_link = "https://raw.githubusercontent.com/virtual-pancakes/met/refs/heads/main/MetaHumanExtraTools/version.json"
    local_dict = json.load(open(local_json_path, "r"))
    try:
        live_dict = json.loads(urllib.request.urlopen(live_json_link).read().decode('utf-8'))
        local_dict["newest_version"] = live_dict["current_version"]
        local_dict["newest_version_changes"] = live_dict["newest_version_changes"]
        local_dict["checked_for_new_version"] = True
    except:
        local_dict["checked_for_new_version"] = False
    json.dump(local_dict, open(local_json_path, "w"), indent=4)
    
    # Load MetaHumanForMaya
    try:
        if not cmds.pluginInfo("MetaHumanForMaya.py", query=True, loaded=True): cmds.loadPlugin("MetaHumanForMaya.py")
    except:
        raise Exception("MetaHumanForMaya plugin not found")
    
    # Install into MetaHuman top menu
    metahuman_menu_items = cmds.menu("MetaHuman", query=True, itemArray=True)
    cmds.menuItem(label="Metahuman Extra Tools", command="import importlib\ntry: importlib.reload(met_gui)\nexcept: import met_gui\nmet_gui.METMainWindow()", parent="MetaHuman", insertAfter=metahuman_menu_items[2])
    print("MetahumanExtraTools loaded")

# Uninitialize the plug-in
def uninitializePlugin(plugin):
    #om2.MFnPlugin(plugin)
    pass