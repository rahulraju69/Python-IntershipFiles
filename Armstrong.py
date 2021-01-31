n=int(input("enter the number:"))
count=0
temp=n
while n>0:
    count=count+1
    n=n//10
print("no of digits:",count)
n,sum=temp,0
while n>0:
    r=n%10
    sum+=r**count
    n=n//10
if sum==temp:
    print(temp,"it is an armstrong")
else:
    print(temp,"not armstrong")