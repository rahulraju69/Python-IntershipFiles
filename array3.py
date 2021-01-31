'''creating an array from an existing array'''
from array import *
arr1=array('i',[10,20,30,40,50])
for i in arr1: print(i)
print("coping arr1 into arr2")
arr2=array(arr1.typecode,(a for a in arr1))
for i in arr2:
    print(i)