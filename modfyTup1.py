'''
modifying tiple by using list func
'''
tup1=(1,2,3,4,5)
print("actual tuple:",tup1)
#modifying the tuple by using list func
list1=list(tup1)
print(type(list1))
list1[3]=6
#again modfy list1
tup1=tuple(list1)
print("aftr modifyning:",tup1)
