# Copyright Virtual Pancakes, 2025. All Rights Reserved.
import maya.cmds as cmds
import met_add_shelf

def main():
    """
    met_add_shelf.create_metahuman_extra_tools_shelf()
    if cmds.menu("MetaHuman", exists=True):
        cmds.menuItem(label="Metahuman Extra Tools", command="import met_gui; met_gui.METMainWindow()", parent="MetaHuman")
    else:
        print("MetaHuman menu not found")
    """
    if not cmds.pluginInfo("MetaHumanExtraTools.py", query=True, loaded=True): cmds.loadPlugin("MetaHumanExtraTools.py")

cmds.scriptJob(event=['DagObjectCreated', main], runOnce=True)