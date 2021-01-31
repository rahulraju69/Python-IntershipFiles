'''accepting n elemets into an array @ runtime and search for an elements'''
from array import*
arr=array("i",[])
n=int(input("enter the number of elements:"))
for i in range(n):
    arr.append(int(input("enter the values:")))
search=int(input("enter the elements to search:"))
for i in arr:
    if i==search:
        print(search,"is found")
else:
        print(search,"not found")