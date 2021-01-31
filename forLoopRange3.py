n=int(input("enter the number:"))
for i in range(2,n,2):    # suppose we give input 30,it will take only upto 28 bcoz of n
    print(i,end=" ")     #if we give n+1 it gives 30



print()
n=int(input("enter the number:"))
for i in range(2,n+1,2):
    print(i,end=" ")