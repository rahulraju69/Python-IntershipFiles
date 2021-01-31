class Base:
    def __init__(self):
        print("Constructor from base")
class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Constructor from Derived")
d1=Derived()
