var=100
def func1():
    var1=10
    print("var1 in func1:",var1)
    def func2():
        nonlocal var1
        var1=var1+20 # it will give error if we wont mention nonlocal in the above
        print("func2 in :",var1)
        return
    func2()

func1()
print("global var:",var)