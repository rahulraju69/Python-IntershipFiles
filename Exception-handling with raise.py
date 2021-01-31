try:
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    if b==0:
        raise Exception ("from raise keyword")
    else:
        c=a/b
except Exception as e:
    print("exception raised",e)
else:
    print("Result:",c)