'''protected-any var that consist of single underscore is known as protected,
it is accessable in the current class and in the derived class but not in the other class
'''

class base:
    def __init__(self):
        self._a=10
        self._b=30
    def display(self):
        print("a=",self._a)
        print("b=",self._b)
class Derived(base):
    def __init__(self):
        super().__init__()

        self.c = self._a + self._b
    def display(self):
        super().display()
        print("sum:",self.c)

d1=Derived()
d1.display()

