#FILE 3 - NURSE DETAILS

import mysql.connector as sqltor
from prettytable import PrettyTable, from_db_cursor
conn=sqltor.connect(host="localhost",user="root",password="root1234",database="HOSPITALMANAGEMENT")
cur=conn.cursor()

cur.execute("USE HOSPITALMANAGEMENT")

#CREATING NURSE DETAILS

cur.execute("""CREATE TABLE IF NOT EXISTS NURSE_DETAILS(NURSEID int,NURSENAME varchar(50),
NURSEAGE int, NURSEDEPT varchar(30), NURSESTATUS char(3), NURSESALARY float,
NURSEGENDER char(1),DATEOFJOINING varchar(15))""")
'''
#MANUAL INSERTION OF DATA
cur.execute("""INSERT INTO NURSE_DETAILS VALUES
(101, 'Ulises Monroy', 25, 'ENT', 'I/P', 15000, 'F', '2021-05-19'),
(102, 'Rashad Steelman', 27, 'PEDIATRICS', 'O/P', 17000, 'M', '2019-04-15'),
(103, 'Conor Pawlitschek', 30, 'DERMOLOGY', 'O/P', 17000, 'M', '2014-10-15'),
(104, 'Axel Ellebracht', 27, 'INTERNAL MEDICINE', 'O/P', 16000, 'M', '2015-01-16')""")
'''

#INSERTION OF DATA

def insert() :
    cur=conn.cursor()
    nid=int(input("Enter nurse id :"))
    nname=input("Enter nurse name :")
    nage=int(input("Enter nurse age :"))
    ndept=input("Enter nurse department :")
    nstatus=input("Enter nurse status :")
    nsal=float(input("Enter nurse salary :"))
    nsex=input("Enter nurse gender :")
    doj=input("Enter nurse date of joining :")
    sql="INSERT INTO NURSE_DETAILS VALUES({},'{}',{},'{}','{}',{},'{}','{}')".format(nid,nname,nage,ndept,nstatus,nsal,nsex,doj)
    cur.execute(sql)
    conn.commit()
    
def updatesalary() :
    cur=conn.cursor()
    nid=int(input("Enter nurse id :"))
    sal=float(input("Enter nurse salary to update :"))
    u1="UPDATE NURSE_DETAILS SET NURSESALARY={} where NURSEID={}".format(sal,nid)
    cur.execute(u1)
    conn.commit()
def updatestatus() :
    cur=conn.cursor()
    nid=int(input("Enter doctor id to update status :"))
    sta=input("Enter new status :")
    u2="UPDATE NURSE_DETAILS SET NURSESTATUS='{}' WHERE NURSEID={}".format(sta,nid)
    cur.execute(u2)
    conn.commit()

def delete() :
    cur=conn.cursor()
    nid=int(input("Enter nurse id to delete :"))
    u5="DELETE FROM NURSE_DETAILS WHERE NURSEID={}".format(nid)
    cur.execute(u5)
    conn.commit()
def search() :
    cur=conn.cursor()
    nid=int(input("Enter nurse id to search for:"))
    u1="SELECT*FROM NURSE_DETAILS WHERE NURSEID={}".format(nid)
    cur.execute(u1)
    data=cur.fetchall()
    if len(data)==0 :
        print("No record found!")
    else :
        print("\nDETAILS :\n")
        for i in data :
            print("NURSE ID :",i[0])
            print("NURSE NAME :",i[1])
            print("NURSE DEPARTMENT",i[3])
            print("NURSE AGE :",i[2])
            print("NURSE STATUS :",i[4])
            print("NURSE SALARY :",i[5])
            print("NURSE GENDER :",i[6])
            print("NURSE DATE OF JOINING :",i[7])
            
        


def display() :
    Y = PrettyTable()
    cur = conn.cursor()
    cur.execute("SELECT*FROM NURSE_DETAILS")
    Y = from_db_cursor(cur)
    print("\nNURSE DETAILS :\n")
    print(Y)
    
'''while True :
    print("=====================================")
    print("            NURSE DETAILS            ")
    print("=====================================")
    print("1. Display nurse details")
    print("2. Search for nurse details")
    print("3. Insert nurse details")
    print("4. Update nurse details")
    print("5. Delete nurse details")
    ch=int(input("Enter choice :"))
    if ch==1 :
        display()
    elif ch==2 :
        search()
    elif ch==3 :
        insert()
    elif ch==4 :
        print("1.Update nurse salary")
        print("2.Update nurse status")
        ch=int(input("Enter choice :"))
        if ch==1 :
            updatesalary()
        elif ch==2 :
            updatestatus()
        else :
            pass
    else :
        print("Please enter valid choice :")'''

     
    


