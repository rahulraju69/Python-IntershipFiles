a=input("enter a string:")
print("Before reverse:",a)
b=a[::-1]
print("After reverse:",b)
if a==b:
    print("palindrome string")
else:
    print("not palindrome string")