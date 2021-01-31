num=input("enter the number:")
n=10
if n==len(num):
    if num.isdigit():
        print(num,"it is valid")
    else:
        print(num,"it is invalid")
else:
    print("please enter only 10 digits number")