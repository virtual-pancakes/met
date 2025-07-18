# Copyright Virtual Pancakes, 2025. All Rights Reserved.
import maya.cmds as cmds

def main():
    if not cmds.pluginInfo("MetaHumanExtraTools.py", query=True, loaded=True): cmds.loadPlugin("MetaHumanExtraTools.py")

cmds.scriptJob(event=['DagObjectCreated', main], runOnce=True)