try:
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    c=a/b
    print(c)
except Exception as e:
    print("exception raised......",e)