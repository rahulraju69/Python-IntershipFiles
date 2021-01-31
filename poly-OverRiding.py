"Overriding-it is the concept of hiding the base class method within derived class method .when the name of method is same in both the base and derived"

class Base:
    def hello(self):
        print("hello from base class")
class Derived(Base):
    def hello(self):
        super().hello()
        print("hello from derived class")
d1=Derived()
d1.hello()
        #if we want both base and derived in output we should use super keyword