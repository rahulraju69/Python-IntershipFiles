n=int(input("enter a value:"))
a=0
b=1
i=1
while i<=n:
    print(a)
    c=a+b
    a,b=b,c
    i+=1