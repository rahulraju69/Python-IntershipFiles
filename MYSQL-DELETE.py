import pymysql
con=pymysql.connect('localhost','root','rahul27','studentdb')
try:
    with con.cursor() as cur:
        trno=input("enter roll no:")
       # tsname=input("enter student name:")
        #tcourse=input("enter course:")
        query="delete from student where rno="+trno
        #print(query)
        cur.execute(query)
        con.commit()
        print("deleted successfully..")

except Exception as e:
    print('exception occured',e)
finally:
    con.close()

