n=int(input("enter the number:"))
try:
    assert n>0
    print("you have entered",n)
except AssertionError:
    print("invalid value entered")