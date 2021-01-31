'''private data-any var consist of double underscore is know as private data member '''

class Student:
    def __init__(self):
        self.__rno=101
        self.name="rahul"
        self.salary=40000
    def Display(self):
        print("roll no:",self.__rno)
        print("Student Name:",self.name)
        print("Salary:",self.salary)

s1=Student()
s1.Display()