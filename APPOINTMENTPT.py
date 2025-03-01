#FILE 4 - APPOINTMENT TABLE
from prettytable import PrettyTable, from_db_cursor
import mysql.connector as sqltor
conn=sqltor.connect(host="localhost",user="root",password="root1234",database="HOSPITALMANAGEMENT")

cur=conn.cursor()

cur.execute("USE HOSPITALMANAGEMENT")

#CREATE TABLE

cur.execute("""CREATE TABLE IF NOT EXISTS APPOINTMENTS(DOCTORID int, DOCTORNAME varchar(50),
TIME1 varchar(15),TIME2 varchar(15),TIME3 varchar(15),TIME4 varchar(15),
TIME5 varchar(15))""")
'''
#MANUAL INSERTION OF DATA
cur.execute("""INSERT INTO APPOINTMENTS VALUES
(1001, 'Dr. Allen Malott', '8:00-8:30', '9:30-10:00', '10:15-10:45', '12:00-12:30', '12:30-12:45'),
(1002, 'Dr. Conner Wigdor', '10:00-10:30', '11:15-11:45', '12:00-12:30', '4:00-4:30', '5:00-5:30'),
(1003, 'Dr. Jonathan Liewald', '4:00-4:15', '4:30-4:45', '5:30-6:00', '6:20-6:50', '8:00-8:30'),
(1004, 'Dr. Richard Weilbacher', '6:45-7:00', '7:00-7:15', '7:15-7:30', '8:00-8:15', '8:30-8:45'),
(1005, 'Dr. Adan Sutphin', '10:00-10:30', '11:00-11:15', '11:30-11:45', '12:00-12:30', '5:00-5:30'),
(1006, 'Dr. Kellen Hossler', '3:15-3:45', '4:00-4:20', '4:30-5:00', '5:00-5:15', '6:30-6:45')""")
'''
def insert() :
    did = int(input("Enter doctor id :"))
    dname=input("Enter doctor name :")
    t1=input("Enter timeslot 1 :")
    t2=input("Enter timeslot 2 :")
    t3=input("Enter timeslot 3 :")
    t4=input("Enter timeslot 4 :")
    t5=input("Enter timeslot 5 :")
    sql="INSERT INTO APPOINTMENTS VALUES({},'{}','{}','{}','{}','{}','{}')".format(did,dname,t1,t2,t3,t4,t5)
    cur=conn.cursor(buffered=True)
    cur.execute(sql)
    
    conn.commit()

def updatet1() :
    cur=conn.cursor()
    did=int(input("Enter doctor id where change has to be made :"))
    nt=input("Enter new time slot :")
    u1="UPDATE APPOINTMENTS SET TIME1='{}' WHERE DOCTORID={}".format(nt,did)
    cur=conn.cursor(buffered=True)
    cur.execute(u1)
    
    conn.commit()
def updatet2() :
    cur=conn.cursor()
    did=int(input("Enter doctor id where change has to be made :"))
    nt=input("Enter new time slot :")
    u1="UPDATE APPOINTMENTS SET TIME2='{}' WHERE DOCTORID={}".format(nt,did)
    cur.execute(u1)
    conn.commit()
def updatet3() :
    cur=conn.cursor()
    did=int(input("Enter doctor id where change has to be made :"))
    nt=input("Enter new time slot :")
    u1="UPDATE APPOINTMENTS SET TIME3='{}' WHERE DOCTORID={}".format(nt,did)
    cur.execute(u1)
    conn.commit()
def updatet4() :
    cur=conn.cursor()
    did=int(input("Enter doctor id where change has to be made :"))
    nt=input("Enter new time slot :")
    u1="UPDATE APPOINTMENTS SET TIME4='{}' WHERE DOCTORID={}".format(nt,did)
    cur.execute(u1)
    conn.commit()
def updatet5() :
    cur=conn.cursor()
    did=int(input("Enter doctor id where change has to be made :"))
    nt=input("Enter new time slot :")
    u1="UPDATE APPOINTMENTS SET TIME5='{}' WHERE DOCTORID={}".format(nt,did)
    cur.execute(u1)
    conn.commit()
def delete() :
    cur=conn.cursor()
    did=int(input("Enter doctor id to delete :"))
    u1="DELETE FROM APPOINTMENTS WHERE DOCTORID={}".format(did)
    cur=conn.cursor(buffered=True)
    cur.execute(u1)
    conn.commit()

def search() :
    cur=conn.cursor()
    did=int(input("Enter doctor id to search for :"))
    u1="SELECT*FROM APPOINTMENTS WHERE DOCTORID={}".format(did)
    cur.execute(u1)
    data=cur.fetchall()
    if len(data)==0 :
        print("No record found!")
    else :
        print("\nDETAILS :\n")
        for i in data :
            print("DOCTOR ID :",i[0])
            print("DOCTOR NAME :",i[1])
            print("TIMESLOT 1 :",i[2])
            print("TIMESLOT 2 :",i[3])
            print("TIMESLOT 3 :",i[4])
            print("TIMESLOT 4 :",i[5])
            print("TIMESLOT 5 :",i[6])

def display() :
    Y = PrettyTable()
    cur = conn.cursor()
    cur.execute("SELECT*FROM APPOINTMENTS")
    Y = from_db_cursor(cur)
    print("\nAPPOINTMENT DETAILS :\n")
    print(Y)

