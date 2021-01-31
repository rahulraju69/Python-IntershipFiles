file1=open("rahulraju.txt","a") #appending to the existing file
n=input("enter your text here:")
print(file1.write(n))
print("successfully done")
file1.close()