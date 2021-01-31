str=input("enter marks in n subjects with space:").split(" ")
print(str)
print(type(str))
marks=[int (i) for i in str]
print("after type casting:")
print(marks)
print("no.of subjects:",len(marks))
print("marks in",len(marks),"subjects")
for i in marks:
    print(i)
tot=sum(marks)
avg=tot/len(marks)
print("total marks:",tot)
print("average marks:",avg)