# creating table with python

import pymysql
con=pymysql.connect('localhost','root','rahul27','studentdb')
try:
    with con.cursor() as cur:
        cur.execute("create table student(rno int primary key,sname varchar(30),course varchar(30))")
        con.commit()
        print('table create successfully')
except Exception as e:
    print('exception occured',e)
finally:
    con.close()

