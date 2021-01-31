import pymysql
con=pymysql.connect('localhost','root','rahul27','studentdb')
try:
    with con.cursor() as cur:
       # trno=input("enter roll no:")
        #tsname=input("enter student name:")
        #tcourse=input("enter course:")
        query= "select * from student"
       # print(query)
        cur.execute(query)
        if cur.rowcount==0:

            print("No rows found")
        else:

            record=cur.fetchone()
            print("roll no:",record[0])
            print("student name:",record[1])
            print("course:",record[2])

            #con.commit()
            print("fetching  successfully..")

except Exception as e:
    print('exception occured',e)
finally:
    con.close()

