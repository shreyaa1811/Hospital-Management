import mysql.connector as sqltor
conn=sqltor.connect(host="localhost",user="root",password="root1234",database="HOSPITALMANAGEMENT")
cur=conn.cursor()

cur.execute("USE HOSPITALMANAGEMENT")

cur.execute("""CREATE TABLE IF NOT EXISTS USERIDS(USERNAME varchar(50),PASSWORD varchar(50))""")
'''cur.execute("INSERT INTO USERIDS VALUES('Jahnvi2019', '2019')")'''
def insert(username,password) :
    cur=conn.cursor()
    sql="INSERT INTO USERIDS VALUES('{}','{}')".format(username,password)
    cur.execute(sql)
    conn.commit()
    
    
