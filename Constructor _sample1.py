'''cons-its is a special member func which is used to initialize mem variable of class'''
'''destructor-it is a garbage colln .it is a mem func used to destroy the obj '''

class Sample: #constructor
    def __init__(self):
        print("constuctor invoked")

class Sample1: #destructor
    def __del__(self):
        print("destructor invoked")
s1=Sample() #cons called here
s1=Sample1() #distructor