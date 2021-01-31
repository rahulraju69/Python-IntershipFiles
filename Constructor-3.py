#const with paramater is known as parameterized const

class Employ:
    def __init__(self,empid,ename,esal):
        self.empid=empid
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Employe id:",self.empid)
        print("Employe Name:",self.ename)
        print("Employe Salary:",self.esal)

e1=Employ(101,"rahul",40000)
e1.display()