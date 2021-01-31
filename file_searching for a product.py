tpid=input("enter product id to search:")
file1=open("file_product","r")
print("list of products:")
for line in file1:
    data=line.split(",")
    if tpid==data[0]:
        print("product name:",data[1])
        print("product price:",data[2])
        break
else:
    print(tpid,"is not found")
file1.close()