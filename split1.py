date="20/10/2020"
s=date.split("/")
print(s)
print(type(s))
for i in s:
    print(i)
print("type casting string into int")
dd=int(s[0])
mm=int(s[1])
yy=int(s[2])
print("date in dd/mm/yy:",dd,"/",mm,"/",yy)