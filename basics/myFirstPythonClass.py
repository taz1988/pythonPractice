class MyFirstClass:
    instanceVariable = "This is an instance variable"

    def __init__(self):
        print("This is the constructor")
        print(self.instanceVariable)

    def methodDefinition(self):
        print("metod called")

    def __del__(self):
        print("deconstructor")

instance = MyFirstClass()
instance.methodDefinition()
