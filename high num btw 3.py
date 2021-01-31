a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a>b and a>c:
    print("a is highest:",a)
if b>a and b>c:
    print("b is highest:",b)
if c>a and c>b:
    print("c is highest:",c)
if a==b and b==c and c==a:
    print("a,b,c are equal")
