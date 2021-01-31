n=int(input("enter the number:"))
sum=0
temp=n
while n>0:
    r=n%10
    sum=(sum*10)+r
    n=n//10
if sum==temp:
    print(temp,"it is palindrome")
else:
    print(temp,"not a palindrome")
