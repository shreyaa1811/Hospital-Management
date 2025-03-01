#FILE 5 - BOOKED APPOINTMENTS
from prettytable import PrettyTable, from_db_cursor
import mysql.connector as sqltor
conn=sqltor.connect(host="localhost",user="root",password="root1234",database="HOSPITALMANAGEMENT")

cur=conn.cursor()

cur.execute("USE HOSPITALMANAGEMENT")

#CREATE TABLE

cur.execute("""CREATE TABLE IF NOT EXISTS BOOKED__APPOINTMENT(PATIENTID int ,
DOCTORID int,
DOCTORNAME varchar(50),
TIMESLOT varchar(15))""")
'''
#INSERTION
cur.execute("INSERT INTO BOOKED__APPOINTMENTS VALUES(50120,1004,'Dr. Richard Weilbacher', 'TIME1')")
'''

def book() :
    Y = PrettyTable()
    cur = conn.cursor()
    cur.execute("SELECT*FROM APPOINTMENTS")
    Y = from_db_cursor(cur)
    print("\nBOOKED APPOINTMENT DETAILS :\n")
    print(Y)
    print()
    pid=int(input("Enter patient id :"))
    did=int(input("Enter doctor id to book appt :"))
    dname=input("Enter doctor name :")
    chosen=input("Enter chosen time slot(Example :TIME1) :")
    cur=conn.cursor()
    sql="INSERT INTO BOOKED__APPOINTMENT VALUES({},{},'{}','{}')".format(pid,did,dname,chosen)
    cur.execute(sql)
    conn.commit()
    u3="UPDATE APPOINTMENTS SET"+" "+chosen+" "+"= 'NULL' WHERE DOCTORID={}".format(did)
    cur.execute(u3)
    conn.commit()
    '''cur.execute("SELECT*FROM APPOINTMENTS")
    data=cur.fetchall()
    print(data)'''
    print("\nAPPOINTMENT BOOKED!\n")
    print("========================")
    print("APPOINTMENT CONFIRMATION")
    print("========================")
    print(pid,":",did,":",dname)
    print("TOTAL CHARGE = AED 50")
    print("\nTHANK YOU FOR BOOKING AN APPOINTMENT AT SILVERWOOD MEDICAL CLINIC\n")
    print("KINDLY REACH THE HOSPITAL 20 MINS PRIOR TO YOUR APPOINTMENT\n")
def bookadmin() :
    Y = PrettyTable()
    cur = conn.cursor()
    cur.execute("SELECT*FROM BOOKED__APPOINTMENT")
    Y = from_db_cursor(cur)
    print("\nDOCTOR DETAILS :\n")
    print(Y)

def updateadmin() :
    cur=conn.cursor()
    pid=int(input("Enter patient id to update:"))
    time=input("Enter updated timeslot :")
    u1="SELECT*FROM BOOKED__APPOINTMENT WHERE PATIENTID={}".format(pid)
    cur.execute(u1)
    data=cur.fetchall()
    for i in data :
        did=i[1]
        otime=i[3]  
    
    u3="UPDATE APPOINTMENTS SET"+" "+time+" "+"= 'NULL' WHERE DOCTORID={}".format(did)

    u="UPDATE BOOKED__APPOINTMENT SET TIMESLOT='{}' WHERE PATIENTID={}".format(time,pid)
    cur.execute(u)
    conn.commit()
    u3="UPDATE APPOINTMENTS SET"+" "+time+" "+"= 'AVAILABLE' WHERE DOCTORID={}".format(did)
    cur.execute(u3)
    conn.commit()


def deleteadmin() :
    cur=conn.cursor()
    pid=int(input("Enter patient id to delete:"))
    u1="DELETE FROM BOOKED__APPOINTMENT WHERE PATIENTID={}".format(pid)
    cur.execute(u1)
    conn.commit()

    
