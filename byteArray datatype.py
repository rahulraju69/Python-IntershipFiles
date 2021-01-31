'''
it is mutable
range from(0-256)
'''
elements=[1,2,3,4,5]
print(elements)
print(type(elements))
x=bytearray(elements)
print(x)
print(type(x))
x[0]=6
for i in x:
    print(i)