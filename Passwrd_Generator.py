import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
#symbols="#$%&*@!,./-_"


all=lower+upper+numbers
length=10
password = "".join(random.sample(all,length))
print(password)