l1=[1,2,3,4,5]
#append
l1.append(6)
print(l1)
#insert
l1.insert(2,6)
print(l1)
#pop
l1.pop()
print(l1)
#copy
l2=[]
l2=l1.copy()
print(l2)

#extend
l3=[1.2,3.5,6.7]
l3.extend(l1)
print(l3)

#reverse
print(l1)
l1.reverse()
print(l1)

#remove
print(l1)
l1.remove(1)
print(l1)

#sort
l1.sort()
print(l1)