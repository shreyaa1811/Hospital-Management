#FILE 1 - DOCTOR DETAILS

import mysql.connector as sqltor
from prettytable import PrettyTable, from_db_cursor
conn=sqltor.connect(host="localhost",user="root",password="root1234",database="HOSPITALMANAGEMENT")
cur=conn.cursor()

cur.execute("USE HOSPITALMANAGEMENT")
cur.execute("""CREATE TABLE IF NOT EXISTS DOCTOR_DETAILS(DOCTORID int,DOCTORNAME varchar(50),
DOCTORDEPT varchar(20),DOCTORAGE int,ROOMNO int,DOCTORSTATUS char(3),
DOCTORSALARY float,DOCTORGENDER char(1),DATEOFJOINING varchar(20),
TIMESLOT varchar(20))""")
'''
#MANUAL INSERTION OF DATA
cur.execute("INSERT INTO DOCTOR_DETAILS VALUES(1001,'Dr. Allen Malott','ENT',32,1,'I/P',20000,'M','2018-05-16','8:00am-2:00pm')")
cur.execute("INSERT INTO DOCTOR_DETAILS VALUES(1002,'Dr. Conner Wigdor','General Medincine',27,2,'I/P',26000,'M','2019-02-19','10:00am-6:00pm')")
cur.execute("INSERT INTO DOCTOR_DETAILS VALUES(1003, 'Dr. Jonathan Liewald', 'Internal Medicine',29,3,'I/P',24000','M','2020-12-09','4:00pm-9:00pm')")
cur.execute("INSERT INTO DOCTOR_DETAILS VALUES(1004, 'Dr. Richard Weilbacher', 'Pulmonologist', 36, 4, 'O/P', 28000, 'M', '2014-02-16', '6:00pm-10:00pm')")
cur.execute("INSERT INTO DOCTOR_DETAILS VALUES(1005, 'Dr. Adan Sutphin', 'Pediatrition', 24, 5, 'I/P', 26000, 'M', '2016-06-02', '10:00am-6:00pm')")
cur.execute("INSERT INTO DOCTOR_DETAILS VALUES(1006, 'Dr. Kellen Hossler', 'Gynaecologist', 32, 6, 'I/P', 26000, 'F', '2017-09-01', '3:00pm-7:00pm')")
'''
#INSERTION OF DATA

def insert() :
    cur=conn.cursor()
    n=int(input("Enter no of entries :"))
    for i in range(n) :
        
        did=int(input("Enter doctor id :"))
        dname=input("Enter doctor name :")
        ddept=input("Enter doctor department :")
        dage=int(input("Enter doctor age :"))
        droom=int(input("Enter doctor room no :"))
        dstatus=input("Enter doctor status :")
        dsal=float(input("Enter doctor salary :"))
        dsex=input("Enter doctor gender :")
        doj=input("Enter doctor date of joining :")
        dtime=input("Enter doctor timeslot :")
        sql="INSERT INTO DOCTOR_DETAILS VALUES({},'{}','{}',{},{},'{}',{},'{}','{}','{}')".format(did,dname,ddept,dage,droom,dstatus,dsal,dsex,doj,dtime)
        cur.execute(sql)
        conn.commit()
    
def updatesalary() :
    cur=conn.cursor()
    did=int(input("Enter doctor id :"))
    sal=float(input("Enter doctor salary to update :"))
    u1="UPDATE DOCTOR_DETAILS SET DOCTORSALARY={} where DOCTORID={}".format(sal,did)
    cur.execute(u1)
#updatesalary()


def updatestatus() :
    cur=conn.cursor()
    did=int(input("Enter doctor id to update status :"))
    sta=input("Enter new status :")
    u2="UPDATE DOCTOR_DETAILS SET DOCTORSTATUS='{}' WHERE DOCTORID={}".format(sta,did)
    cur.execute(u2)
   
def updateroomno() :
    cur=conn.cursor()
    did=int(input("Enter doctor id to update status :"))
    room=int(input("Enter updated room no :"))
    u3="UPDATE DOCTOR_DETAILS SET ROOMNO={} WHERE DOCTORID={}".format(did,room)
    cur.execute(u3)

def updatetimeslot() :
    cur=conn.cursor()
    did=int(input("Enter doctor id to update status :"))
    ts=input("Enter updated time slot :")
    u4="UPDATE DOCTOR_DETAILS SET TIMESLOT='{}' WHERE DOCTORID={}".format(ts,did)
    cur.execute(u4)
    conn.commit()

def deletedoctor() :
    cur=conn.cursor()
    did=int(input("Enter doctor id to delete :"))
    u5="DELETE FROM DOCTOR_DETAILS WHERE DOCTORID={}".format(did)
    cur.execute(u5)
    conn.commit()

def search() :
    cur=conn.cursor()
    did=int(input("Enter doctor id to search for:"))
    u1="SELECT*FROM DOCTOR_DETAILS WHERE DOCTORID={}".format(did)
    cur.execute(u1)
    data=cur.fetchall()
    if len(data)==0 :
        print("No record found!")
    else :
        print("\nDETAILS :\n")
        for i in data :
            print("DOCTOR ID :",i[0])
            print("DOCTOR NAME :",i[1])
            print("DOCTOR DEPARTMENT",i[2])
            print("DOCTOR AGE :",i[3])
            print("DOCTOR ROOM :",i[4])
            print("DOCTOR STATUS :",i[5])
            print("DOCTOR SALARY :",i[6])
            print("DOCTOR GENDER :",i[7])
            print("DOCTOR DATE OF JOINING :",i[8])
            print("DOCTOR TIMESLOT :",i[9])
        
    
def  display():
    Y = PrettyTable()
    cur = conn.cursor()
    cur.execute("SELECT*FROM DOCTOR_DETAILS")
    Y = from_db_cursor(cur)
    print("\nDOCTOR DETAILS :\n")
    print(Y)
'''
while True :
    print("=====================================")
    print("           DOCTOR DETAILS            ")
    print("=====================================")
    print("1. Display doctor details")
    print("2. Search for doctor details")
    print("3. Insert doctor details")
    print("4. Update doctor details")
    print("5. Delete doctor details")
    ch=int(input("Enter choice :"))
    if ch==1 :
        display()
    elif ch==2 :
        search()
    elif ch==3 :
        insert()
    elif ch==4 :
        print("1.Update doctor status")
        print("2.Update doctor room number")
        print("3.Update doctor timeslot")
        ch=int(input("Enter choice :"))
        if ch==1 :
            updatestatus()
        elif ch==2 :
            updateroomno()
        elif ch==3 :
            updatetimeslot()
        else :
            pass
    elif ch==5 :
        deletedoctor()
    else :
        print("Please enter valid choice :")'''



