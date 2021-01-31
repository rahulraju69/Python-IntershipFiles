try:
    empid=int(input("enter the emp id:"))
except Exception as f:
    print("Exception raised:",f)
else:
    print("Emp id:",empid)
finally:
    print("i will run compulsory")