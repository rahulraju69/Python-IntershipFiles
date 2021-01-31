# connecting to mysql database

import pymysql
try:
    con=pymysql.connect('localhost','root','rahul27','Studentdb')
    print("connected to mysql successfully..")
except Exception as e:
    print("Exception occured:",e)
else:
    con.close()