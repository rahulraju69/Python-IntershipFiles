#creating an array of n elements
#searching an array with index

from array import*
arr=array("i",[])
n=int(input("enter n value:"))
for i in range(n):
    arr.append(int(input("enter elements to insert:")))
try:
    s=int(input("enter element to search:"))
    pos=arr.index(s)
    print("the element is found in arr[",pos,"]")
except:
    print(s,"not found")