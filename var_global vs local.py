a=10 #global var
def hello():
    a=20 #local var
    print("a value in hello:",a) #local a
    return
hello()
print("a value outside in hello:",a) #global a