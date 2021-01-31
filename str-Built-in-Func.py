'''built-in function
len(),join,split,upper,lower,isupper,islower,isdigit,isalnum,title,strip
rstrip,lstrip,swap
'''

print("len:")
str1="rahul"
print(len(str1))

print()
print("join:")
str1=["rahul","raju","vinay"]
print("@".join(str1))

print()
print("concatinate:")

str1="rahul"
str2="raju"
fullName=str1+str2
print(fullName)

print()
print("upper:") #small letter becomes cap
str1="rahul"
print(str1.upper())

print()
print("lower:") #cap letter becomes samller
str1="rahul"
print(str1.lower())

print()
print("islower:") #if all letters are small it prints true otherwise false
str1="rahul"
print(str1.islower())


print()
print("isupper:") #if all letters are small it prints true
str1="RAHUL"
print(str1.isupper())

print()
print("title:") #title prints only first letter of word capital
str1="rahul raju"
print(str1.title())

print()
print("isdigit:") #it prits only numbers not spl.char r alpha
str1="9550989692"
print(str1.isdigit())


print()
print("isalnum:") #it prits only numbers and alpha alnum-alphabets either numbers
str1="rahul"
print(str1.isalnum())

print()
print("strip:") #it remove spaces from left n right
str1="   rahul   "
print(len(str1)) #o/p is 11 bcoz of spaces
s=str1.strip()
print(len(s))


print()
print("rstrip:") #it remove spaces from left n right
str1="rahul   "
print(len(str1)) #o/p is 11 bcoz of spaces
s=str1.rstrip()
print(len(s))

print()
print("lstrip:") #it remove spaces from left n right
str1="   rahul"
print(len(str1)) #o/p is 11 bcoz of spaces
s=str1.lstrip()
print(len(s))

print()
print("swapcase:") #it is used for snall-big,big-small coversion
str1= "HellOImRaHuL"
print(str1.swapcase())







