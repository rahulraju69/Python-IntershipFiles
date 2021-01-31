#Swapping of two numbers using third variable
#1st method

a=10
b=20
print("Before swap a=",a ,"b=",b)
c=a
a=b
b=c
print("After swap a=",a,"b=",b)


#2nd method

a=10
b=20
print("Before swap a=",a ,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swap a=",a ,"b=",b)