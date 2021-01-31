#multiple-it consist of 2 parents one child

class First:
    def hello1(self):
        print("Method1 from first...")

class Second:
    def hello2(self):
        print("Method2 from first...")

class Result(First,Second):
    pass
r1=Result()
r1.hello1()
r1.hello2()