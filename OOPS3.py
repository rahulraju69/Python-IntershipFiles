#student marks list with class

class Student:

    def accept(self):
        self.rno=int(input("enter the roll number:"))
        self.name=input("enter the name:")
        self.s1=int(input("enter marks in sub1:"))
        self.s2=int(input("enter marks in sub2:"))
        self.s3=int(input("enter marks in sub3:"))

    def cal(self):
        self.tot=self.s1+self.s2+self.s3
        self.avg=self.tot/3

    def dispaly(self):
        print("rno:",self.rno)
        print("Student name:",self.name)
        print("total:",self.tot)
        print("average:",self.avg)
k1=Student()
k1.accept()
k1.cal()
k1.dispaly()