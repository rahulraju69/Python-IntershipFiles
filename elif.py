'''
using switch case implementation
'''

a=int(input("enter a number:"))
b=int(input("enter b number:"))
print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
ch=int(input("enter your choice:"))
if ch==1:
    print("the sum is:",a+b)
elif ch==2:
    print("the sub is:",a-b)
elif ch==3:
    print("the mul is:",a*b)
elif ch==4:
    print("the div is:",a/b)
else:
    print("Out of boundary")