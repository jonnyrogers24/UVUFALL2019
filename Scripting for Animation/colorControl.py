import maya.cmds as cmds

def colorControl (color):
    if color == 'yellow':
        color = 17
    elif color == 'blue':
        color = 6
    elif color == 'red':
        color = 13
    else:
        color = 5
        
    sels = cmds.ls(sl=True)
    
    for sel in sels: 
        shapes = cmds.listRelatives(sel, children=True, shapes=True)
    
        for shape in shapes: 
            cmds.setAttr('%s.overrideEnabled' % shape, True)
            cmds.setAttr('%s.overrideColor' % shape, color)
    
colorControl ('other')