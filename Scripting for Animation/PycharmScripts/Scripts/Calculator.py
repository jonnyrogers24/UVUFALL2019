def Calculator(operation, nums):
    '''

    Enter operation to be performed

    -------------------------------

    **AVAILABLE OPERATIONS**

    Operation 1 = Addition , Enter Values
    Operation 2 = Subtraction , Enter Values
    Operation 3 = Multiplication , Enter Values
    Operation 4 = Division , Enter Values
    Operation 5 = Mean , Enter Values
    Operation 6 = Median , Enter Values
    Operation 7 = Power , Enter 2 Values (num, exponent)

    '''

    if (operation == 1):
        total = (Add(nums))

    if (operation == 2):
        total = (Sub(nums))

    if (operation == 3):
        total = (Mult(nums))

    if (operation == 4):
        total = (Div(nums))

    if (operation == 5):
        total = (Mean(nums))

    if (operation == 6):
        total = (Median(nums))

    return total


# 1 = Addition#
def Add(values):
    sum = 0
    for val in values:
        sum = sum + val
    return sum


# 2 = subdivision#
def Sub(values):
    sum = 0
    for val in values:
        sum = sum - val
    return sum


# 3 = Multiplication#
def Mult(values):
    sum = 1
    for val in values:
        sum = sum * val
    return sum


# 4 = Division#
def Div(values):
    sum = values[0]
    for val in values[1:]:
        sum = sum / val
    return sum


# 5 = Mean#
def Mean(values):
    sum = 0
    for val in values:
        sum = sum + val
        average = sum / len(values)
    return average


# 6 = Median#
def Median(values):
    values = sorted(values)
    print("Values Sorted:")
    print values
    sortedValues = len(values)
    print("Number of Values")
    print sortedValues

    if (sortedValues % 2 != 0):
        middleValue = (sortedValues / 2)
        median = values[middleValue]
        print ("Median:")
        print median

    if (sortedValues % 2 == 0):
        middleValue = (sortedValues / 2)
        median = (values[middleValue] + values[middleValue - 1]) / 2
        print ("Median is:")
        print median

    return median


# 7 = Power#
def Power(value, exp):
    total = pow(value, exp)
    return total