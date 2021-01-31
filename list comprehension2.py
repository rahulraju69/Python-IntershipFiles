# 1 to 10 sq number
print("without list compr")
list1=[]
for i in range(1,11):
    list1.append(i*i)
print(list1)

print()
print("with list compr")

list2=[ i*i for i in range(1,11)]
print(list2)
