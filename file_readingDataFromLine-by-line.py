file1=open("file_product","r")
print("list of products:")
for line in file1:
    data=line.split(",")
    print(data[0],"\t",data[1],"\t",data[2],"\t")
file1.close()