Current=int(input("enter the current year:"))
Born=int(input("enter the born year:"))
s1=Current-Born
if s1>=18:
    print("your age is",s1,"years")
    print("your are major")
else:
    print("your age is",s1,"years")
    print("you are minor")