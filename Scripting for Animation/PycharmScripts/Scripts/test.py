import maya.cmds as cmds

cmds.polysphere(axis=[1, 0, 0], radius=5, name='Ball', constructionHistory=True)
cmds.polyCube(d=3, h=1,w=5, n='Box')

cmds.xform('Ball', ws=True, translation=[5, 8, 10])
