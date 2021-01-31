itemCode=int(input("enter the item code:"))
itemName=input("enter the item name:")
price=int(input("enter the price:"))
numberOfItems=int(input("enter the no of items:"))
amount=price*numberOfItems
discount=50
netbill=amount-discount
print("itemcode:",itemCode)
print("itemName:",itemName)
print("price:",price)
print("number of item:",numberOfItems)
print("amount:",amount)
print("discount:",discount)
print("netbill:",netbill)