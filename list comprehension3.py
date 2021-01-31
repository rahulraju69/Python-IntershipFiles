# 1 to 20 even num
print("without list compr")

list1=[]
for i in range(0,21):
    if i%2==0:
        list1.append(i)
print(list1)

print()
print("with list compr")
list2=[ i for i in range(0,21) if i%2==0]
print(list2)
