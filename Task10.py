a=int(input("enter a number:"))
b=int(input("enter b number:"))
print("1.+ \n 2.- \n 3.* \n 4./")
ch=str(input("enter your choice:"))
if ch=="+":
    print("the sum is:",a+b)
elif ch=="-":
    print("the sub is:",a-b)
elif ch=="*":
    print("the mul is:",a*b)
elif ch=="/":
    print("the div is:",a/b)
else:
    print("Out of boundary")