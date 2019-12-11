import maya.cmds as cmds


class Toolbox():
    def __init__(self):
        self.main_window = "JRogers ToolBox"
        self.sub_window_color = "Color Changer"
        self.sub_window_calculator = "Calculator"

    def create(self):
        self.delete()

        self.main_window = cmds.window(self.main_window)
        self.m_column = cmds.columnLayout(p=self.main_window, adj=True)
        cmds.showWindow(self.main_window)
        cmds.button(p=self.m_column,
                    label='Open Color Control Window',
                    c=lambda *args: self.colorChange())
        cmds.button(p=self.m_column,
                    label='Open Calculator',
                    c=lambda *args: self.calculatorTool())

    def calculatorTool(self):
        self.delete()

        self.sub_window_calculator = cmds.window(self.sub_window_calculator)
        self.m_column = cmds.columnLayout(p=self.sub_window_calculator, adj=True)

        cmds.showWindow(self.sub_window_calculator)

        cmds.text(p=self.m_column,
                  label="**AVAILABLE OPERATIONS**")
        cmds.text(p=self.m_column,
                  label="Operation 1 = Addition , Enter Values")
        cmds.text(p=self.m_column,
                  label="Operation 2 = Subtraction , Enter Values")
        cmds.text(p=self.m_column,
                  label="Operation 3 = Multiplication , Enter Values")
        cmds.text(p=self.m_column,
                  label="Operation 4 = Division , Enter Values")
        cmds.text(p=self.m_column,
                  label="Operation 5 = Mean , Enter Values")
        cmds.text(p=self.m_column,
                  label="Operation 6 = Median , Enter Values")
        cmds.text(p=self.m_column,
                  label="Operation 7 = Power , Enter 2 Values (num, exponent)")
        self.operation = cmds.textField(p=self.m_column,
                                        placeholderText='Enter Operation Number')
        self.nums = cmds.textField(p=self.m_column,
                                   placeholderText='Enter Values')
        cmds.button(p=self.m_column,
                    label='Calculate',
                    c=lambda *args: self.calcBtn())

    def calcBtn(self):
        value1 = cmds.textField(self.operation, q=True, text=True)
        value2 = cmds.textField(self.nums, q=True, text=True)
        self.calculator(value1, value2)
        cmds.textField(self.operation, e=True, text='')
        cmds.textField(self.nums, e=True, text='')

    def colorChange(self):

        self.sub_window_color = cmds.window(self.sub_window_color)
        self.m_column = cmds.columnLayout(p=self.sub_window_color, adj=True)

        cmds.showWindow(self.sub_window_color)

        cmds.text(p=self.m_column,
                  label='1. Click "Create PolySphere Button"')
        cmds.button(p=self.m_column,
                    label='Create PolySphere',
                    c=lambda *args: cmds.polySphere())
        cmds.text(p=self.m_column,
                  label='2. With Object Selected, Click On Color From Options Below to Change Wire Frame Color')
        cmds.button(p=self.m_column,
                    label='Yellow',
                    c=lambda *args: self.colorControl('yellow'))
        cmds.button(p=self.m_column,
                    label='Red',
                    c=lambda *args: self.colorControl('red'))
        cmds.button(p=self.m_column,
                    label='Pink',
                    c=lambda *args: self.colorControl('pink'))
        cmds.button(p=self.m_column,
                    label='Black',
                    c=lambda *args: self.colorControl('black'))
        cmds.button(p=self.m_column,
                    label='Green',
                    c=lambda *args: self.colorControl('green'))
        cmds.button(p=self.m_column,
                    label='Default',
                    c=lambda *args: self.colorControl(''))
        self.color = cmds.textField(p=self.m_column,
                                    placeholderText='Enter Color Name Here')
        cmds.button(p=self.m_column,
                    label='Change Color',
                    c=lambda *args: self.colorBtn())

    def colorBtn(self):
        value = cmds.textField(self.color, q=True, text=True)
        self.colorControl(value)
        cmds.textField(self.color, e=True, text='')

    def delete(self):
        if cmds.window(self.main_window, exists=True):
            cmds.deleteUI(self.main_window)
        if cmds.window(self.sub_window_color, exists=True):
            cmds.deleteUI(self.sub_window_color)
        if cmds.window(self.sub_window_calculator, exists=True):
            cmds.deleteUI(self.sub_window_calculator)

    def colorControl(self, color):
        if color == 'yellow':
            color = 17
        elif color == 'blue':
            color = 6
        elif color == 'red':
            color = 13
        elif color == 'black':
            color = 1
        elif color == 'green':
            color = 27
        elif color == 'pink':
            color = 9
        else:
            color = 5

        sels = cmds.ls(sl=True)

        for sel in sels:
            shapes = cmds.listRelatives(sel, children=True, shapes=True)

            for shape in shapes:
                cmds.setAttr('%s.overrideEnabled' % shape, True)
                cmds.setAttr('%s.overrideColor' % shape, color)

    def calculator(self, operation, nums):

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

        if operation == 1:
            total = (self.Add(nums))
            print(total)
            return total

        elif operation == 2:
            total = (self.Sub(nums))
            print(total)
            return total

        elif operation == 3:
            total = (self.Mult(nums))
            print(total)
            return total

        elif operation == 4:
            total = (self.Div(nums))
            print(total)
            return total

        elif operation == 5:
            total = (self.Mean(nums))
            print(total)
            return total

        elif operation == 6:
            total = (self.Median(nums))
            print(total)
            return total

        elif operation == 6:
            total = (self.Power(nums))
            print(total)
            return total

            # 1 = Addition#
    def Add(self, values):
        sum = 0
        for val in values:
            sum = sum + val
            print(sum)
        return sum

    # 2 = subdivision#
    def Sub(self, values):
        sum = 0
        for val in values:
            sum = sum - val
            print(sum)
        return sum

    # 3 = Multiplication#
    def Mult(self, values):
        sum = 1
        for val in values:
            sum = sum * val
            print(sum)
        return sum

    # 4 = Division#
    def Div(self, values):
        sum = values[0]
        for val in values[1:]:
            sum = sum / val
            print(sum)
        return sum

    # 5 = Mean#
    def Mean(self, values):
        sum = 0
        for val in values:
            sum = sum + val
            average = sum / len(values)
            print(average)
        return average

    # 6 = Median#
    def Median(self, values):
        values = sorted(values)
        print("Values Sorted:")
        print
        values
        sortedValues = len(values)
        print("Number of Values")
        print
        sortedValues

        if (sortedValues % 2 != 0):
            middleValue = (sortedValues / 2)
            median = values[middleValue]
            print("Median:")
            print
            median

        if (sortedValues % 2 == 0):
            middleValue = (sortedValues / 2)
            median = (values[middleValue] + values[middleValue - 1]) / 2
            print("Median is:")
            print(median)

        return median

    # 7 = Power#
    def Power(self, value, exp):
        total = pow(value, exp)
        print(total)
        return total


myToolBoxWindow = Toolbox()
myToolBoxWindow.create()
