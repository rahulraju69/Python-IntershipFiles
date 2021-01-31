#handling two exception at a time
try:
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    c=a/b
except (ZeroDivisionError,ValueError) as e:
    print("exception raised..",e)
else:
    print("result",c)