class Employ:
    def __init__(self):
        self.roll=1001
        self.name="rahul"
        self.sal=40000

    def display(self):
        print("Roll no:",self.roll)
        print("Name:",self.name)
        print("Salary:",self.sal)

    def __del__(self):
        print("Destructor invoked")

e1=Employ()
e1.display()
print("doc String:",e1.__doc__)
print("Module:",e1.__module__)
print("Dict:",e1.__dict__)
print("Name:",Employ.__name__)
