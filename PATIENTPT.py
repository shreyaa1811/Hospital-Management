#FILE 1 - PATIENT DETAILS
from prettytable import PrettyTable, from_db_cursor
import mysql.connector as sqltor
conn=sqltor.connect(host="localhost",user="root",password="root1234")
cur=conn.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS HOSPITALMANAGEMENT")
cur.execute("USE HOSPITALMANAGEMENT")

cur.execute("""CREATE TABLE IF NOT EXISTS PATIENTDETAILS(PATIENTID int,
PATIENTNAME varchar(50),
PATIENTAGE int, PATIENTGENDER char(1),PATIENTPHONE int,
DATEOFREGISTRATION varchar(20))""")

#MANUAL INSERTION OF DATA
cur.execute("INSERT INTO PATIENTDETAILS VALUES(50120, 'Jahnvi Singh', 35, 'F', 501061982, '2019-04-23')")

def search() :
    cur=conn.cursor()
    pid=int(input("Enter id to search for:"))
    u1="SELECT*FROM PATIENTDETAILS WHERE PATIENTID={}".format(pid)
    cur.execute(u1)
    data=cur.fetchall()
    if len(data)==0 :
        print("No record found!")
    else :
        print("\nDETAILS :\n")
        for i in data :
            print("PATIENT ID :",i[0])
            print("PATIENT NAME :",i[1])
            print("PATIENT  AGE :",i[2])
            print("PATIENT GENDER :",i[3])
            print("PATIENT PHONE :",i[4])
            print("PATIENT DATE OF REGISTRATION :",i[5])
            
def display() :
    Y = PrettyTable()
    cur = conn.cursor()
    cur.execute("SELECT*FROM PATIENTDETAILS")
    Y = from_db_cursor(cur)
    print("\nPATIENT DETAILS :\n")
    print(Y)

   
def insert() :
    cur=conn.cursor()
    pid=int(input("Enter patient id :"))
    pname=input("Enter patient name :")
    page=int(input("Enter patient age :"))
    pgen=input("Enter patient gender :")
    ph=int(input("Enter phone number :"))
    dor=input("Enter date of registration :")
    sql="INSERT INTO PATIENTDETAILS VALUES({},'{}',{},'{}',{},'{}')".format(pid,pname,page,pgen,ph,dor)
    cur.execute(sql)
    conn.commit()


def delete() :
    cur=conn.cursor()
    pid=int(input("Enter patient id to delete:"))
    sql="DELETE FROM PATIENTDETAILS WHERE PATIENTID={}".format(pid)
    cur.execute(sql)
    conn.commit()

def updatedor() :
    cur=conn.cursor()
    pid=int(input("Enter patient id to update:"))
    dor=input("Enter updated date of registration :")
    sql="UPDATE PATIENTDETAILS SET DATEOFREGISTRATION='{}' WHERE PATIENTID={}".format(dor,pid)
    cur.execute(sql)
    conn.commit()
    
def updateage() :
    cur=conn.cursor()
    pid=int(input("Enter patient id to update:"))
    age=int(input("Enter updated patient age :"))
    sql="UPDATE PATIENTDETAILS SET PATIENTAGE={} WHERE PATIENTID={}".format(age,pid)
    cur.execute(sql)
    conn.commit()

def updateph() :
    cur=conn.cursor()
    pid=int(input("Enter patient id to update:"))
    ph=int(input("Enter updated phone number :"))
    sql="UPDATE PATIENTDETAILS SET PATIENTPHONE={} WHERE PATIENTID={}".format(ph,pid)
    cur.execute(sql)
    conn.commit()
    
'''   
while True :
    print("=====================================")
    print("            PATIENT DETAILS          ")
    print("=====================================")
    print("1. Display patient details")
    print("2. Search for patient details")
    print("3. Update patient details")
    print("4. Delete patient details")
    print("5. Return to previous menu")
    ch=int(input("Enter choice :"))
    if ch==1 :
        display()
    elif ch==2 :
        search()
    elif ch==3 :
        print("1.Update date of registration")
        print("2.Update patient age")
        print("3.Update patient phone no")
        chs=int(input("Enter choice :"))
        if chs==1 :
            updatedor()
        elif chs==2 :
            updateage()
        elif chs==3 :
            updateph()
        else :
            pass
    elif ch==4 :
        delete()
    else :
        print("PLEASE ENTER A VALID CHOICE!")'''

