#single- it consist of 1 parent 2 child

class First:
    def hello1(self):
        print("hello from first...")
class Second(First): #inheriting 1st class into second
    def hello2(self):
        print("hello from second...")

s1=Second() #creating obj of 2nd func
s1.hello1()
s1.hello2()

