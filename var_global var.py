a=10
def hello():
    global a
    a=a+20 # it will show error bcoz we have to use global keyword in the above
    print("a value in hello",a)
    return
hello()
print("a outside the func",a)
hello()
print("a outside the func",a)
