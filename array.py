import array
arr=array.array("i",[10,20,30,40])
print(arr)
print("first elements:",arr[0])
print("last elements:",arr[-1])
print("slicing elements:",arr[1:])
print("reverse elements:",arr[::-1])

for i in arr:
    print(i)