
try:
    empid=int(input("enter employee id:"))
    print("empid:",empid)
except Exception as e:
    print("Exception raised....!",e)
    print(type(e))
else:
    print("Empid:",empid)