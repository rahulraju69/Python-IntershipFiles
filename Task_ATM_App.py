#ATM Application Using Function With Infinite Loop
import sys
bal=7000
minbal=5000
avbal=0

def deposite():
    temp=int(input("Enter amount to deposite:"))
    print("Rs.",temp,"is deposited successfully")
    return temp
def withdraw():
    temp=int(input("Enter amount to draw:"))
    avbal=bal-minbal
    if temp<=avbal:
        print("please collect your cash here..")
        return temp
    else:
        print("Insufficient Funds...")
        return 0
def showBalance():
    avbal=bal-minbal
    print("Total Balance:",bal)
    print("Available Balance:",avbal)
    return

while (True):
    print("1. Deposite")
    print("2. Withdraw")
    print("3. ShowBalance")
    print("4.  Exit")

    ch=int(input("enter your choice:"))
    if ch==1:
        d=deposite()
        bal+=d
    elif ch==2:
        w=withdraw()
        bal-=w
    elif ch==3:
        showBalance()
    elif ch==4:
        print("-----THANKS FOR BANKING WITH US-----")
        sys.exit(0)
    else:
        print("INVALID CHOICE.....!")