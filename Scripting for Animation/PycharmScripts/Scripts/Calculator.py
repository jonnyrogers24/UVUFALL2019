import maya.cmds as cmds
def Add(values):
    '''
    Adds two numbers together and returns result
    input: float/int value1, float/int values2
    return: float
    '''

    sum=0
    for val in values:
        sum += val

    return sum

def Power(value, power):
    import math
    return math.pow(value, power)