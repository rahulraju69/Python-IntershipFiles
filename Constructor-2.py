#constructor without parameter is said to be default cons
class Employ:
    def __init__(self):
        self.empid=1001
        self.name="rahul"
        self.sal=40000
    def display(self):
        print("Empid:",self.empid)
        print("Name:",self.name)
        print("Salary:",self.sal)

e1=Employ()
e1.display()
