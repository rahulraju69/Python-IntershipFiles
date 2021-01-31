'''
is allows only range of (0-256)
it is mutuable
it allows only postive values,dnot allow strings and negative values
'''

element=[10,20,30,40]
print(type(element))
x=bytes(element)
print(x)
print(type(x))
print("elements of all in x:")
for i in x:
    print(i)
