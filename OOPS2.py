#passing argyments in the func
class Sum:
    def accept(self,num1=2,num2=2):
        self.num1=num1
        self.num2=num2
    def display(self):
        print("num1:",self.num1)
        print("num2:",self.num2)
        print("sum:",self.num1+self.num2)

k1=Sum()
k1.accept()
k1.display()