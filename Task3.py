Empid=int(input("enter the empid:"))
name=input("enter the name:")
BasicSalary=int(input("enter the basic salary:"))
TA=1000
DA=2000
HRA=3000
PF=1000
IT=500
GROSS=BasicSalary+TA+DA+HRA
NET=GROSS-(PF+IT)
print("-------EmployeeId---------")
print("EmployeeId:",Empid)
print("EmployeeName:",name)
print("EmployeeBaseSalary:",BasicSalary)
print("GROSS PAY:",GROSS)
print("NET PAY:",NET)