n=int(input("enter the number:"))
if n<10:
    print("one digit")
if n>=10 and n<100:
    print("Two digits")
if n<1000 and n>100:
    print("three digits")
if n>1000 and n<10000:
    print("four digits")