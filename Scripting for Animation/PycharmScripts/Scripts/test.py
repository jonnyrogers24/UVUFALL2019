import maya.cmds as cmds

sels = cmds.ls(sl=True)
print sels[0]

numInt = 3
numFloat = 6.3

print numInt
print numFloat

sels = "hello"
print sels

students = [['bill', 'bob', 'candace', 'rebecca'],
            [100,98,67,37],
            ['Clayton', 'Clayton', 'Clayton','Clayton']]
print students[0][3], 'respects' , students[2][0]

for i in range(len(students[0])):
    print 'Name:', students[0][i]
    print 'Score', students[1][i]
    print 'Teacher', students[2][i]
    print '-----------------------'
print 'Complete'

for name in students[0]:
    print name, 'is great!'

for i in range(len(students)):
    print students[i]
    print i

print "done"