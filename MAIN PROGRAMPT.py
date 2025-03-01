#MAIN PROGRAM

import USERIDPT
import PATIENTPT
import DOCTORPT
import NURSEPT
import APPOINTMENTPT
import BOOKEDAPPOINTMENTPT
from prettytable import PrettyTable, from_db_cursor
import mysql.connector as sqltor
conn=sqltor.connect(host="localhost",user="root",password="root1234",database="HOSPITALMANAGEMENT")
cur=conn.cursor()


def doctortable() :
 
    while True :
        print("=====================================")
        print("           DOCTOR DETAILS            ")
        print("=====================================")
        print("1. Display doctor details")
        print("2. Search for doctor details")
        print("3. Insert doctor details")
        print("4. Update doctor details")
        print("5. Delete doctor details")
        print("6. Return to previous menu")
        ch=int(input("Enter choice :"))
        if ch==1 :
            DOCTORPT.display()
        elif ch==2 :
            DOCTORPT.search()
        elif ch==3 :
            DOCTORPT.insert()
        elif ch==4 :
            print("1.Update doctor status")
            print("2.Update doctor room number")
            print("3.Update doctor timeslot")
            print("4.Update doctor salary")
            ch=int(input("Enter choice :"))
            if ch==1 :
                DOCTORPT.updatestatus()
            elif ch==2 :
                DOCTORPT.updateroomno()
            elif ch==3 :
                DOCTOR.updatetimeslot()
            elif ch==4 :
                DOCTORPT.updatesalary()
            else :
                pass
        elif ch==5 :
            DOCTORPT.deletedoctor()
        elif ch==6 :
            break
        else :
            print("\nPLEASE ENTER VALID CHOICE!")

def nurse() :
    
    while True :
        print("=====================================")
        print("            NURSE DETAILS            ")
        print("=====================================")
        print("1. Display nurse details")
        print("2. Search for nurse details")
        print("3. Insert nurse details")
        print("4. Update nurse details")
        print("5. Delete nurse details")
        print("6. Return to previous menu")
        ch=int(input("Enter choice :"))
        if ch==1 :
            NURSEPT.display()
        elif ch==2 :
            NURSEPT.search()
        elif ch==3 :
            NURSEPT.insert()
        elif ch==4 :
            print("1.Update nurse salary")
            print("2.Update nurse status")
            ch=int(input("Enter choice :"))
            if ch==1 :
                NURSEPT.updatesalary()
            elif ch==2 :
                NURSEPT.updatestatus()
            else :
                pass
        elif ch==5 :
            NURSEPT.delete()
        elif ch==6 :
            break
        else :
            print("Please enter valid choice!")

         
def patientadmin() :
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
            PATIENTPT.display()
        elif ch==2 :
            PATIENTPT.search()
        elif ch==3 :
            print("1.Update date of registration")
            print("2.Update patient age")
            print("3.Update patient phone no")
            chs=int(input("Enter choice :"))
            if chs==1 :
                PATIENTPT.updatedor()
            elif chs==2 :
                PATIENTPT.updateage()
            elif chs==3 :
                PATIENTPT.updateph()
            else :
                pass
        elif ch==4 :
            PATIENTPT.delete()
        elif ch==5 :
            break
        
        else :
            print("PLEASE ENTER VALID CHOICE!")
                
def appointments() :
    while True :
        print("=====================================")
        print("             APPOINTMENTS            ")
        print("=====================================")
        print("1.View Appointments")
        print("2.Search for Appointments")
        print("3.Insert new appointment")
        print("4.Update appointment")
        print("5.Delete appointment")
        print("6.Return to previous menu")
        ch=int(input("Enter choice :"))
        if ch==1 :
            APPOINTMENTPT.display()
        elif ch==2 :
            APPOINTMENTPT.search()
        elif ch==3 :
            APPOINTMENTPT.insert()
        elif ch==4 :
            print("1.UPDATE T1")
            print("2.UPDATE T2")
            print("3.UPDATE T3")
            print("4.UPDATE T4")
            print("5.UPDATE T5")
            chs=int(input("Enter choice :"))
            if chs==1 :
                APPOINTMENTPT.updatet1()
            elif chs==2 :
                APPOINTMENTPT.updatet2()
            elif chs==3 :
                APPOINTMENTPT.updatet3()
            elif chs==4 :
                APPOINTMENTPT.updatet4()
            elif chs==5 :
                APPOINTMENTPT.updatet5()
            else :
                pass
            
        elif ch==5 :
            APPOINTMENTPT.delete()
        elif ch==6  :
            break
        else :
            print("\nPLEASE ENTER VALID CHOICE!")
                 


def bookappt() :
    while True :
        print("==================================")
        print("        BOOKED APPOINTMENTS       ")
        print("==================================")
        print("1. View Booked appointments")
        print("2. Update Booked appointments")
        print("3. Delete Booked appointments")
        print("4. Return to previous menu")
        ch=int(input("Enter choice :"))
        if ch==1 :
            BOOKEDAPPOINTMENTPT.bookadmin()
        elif ch==2 :
            BOOKEDAPPOINTMENTPT.updateadmin()
        elif ch==3 :
            BOOKEDAPPOINTMENTPT.deleteadmin()
        elif ch==4 :
            break
       
        else :
            print("\nPLEASE ENTER VALID CHOICE!\n")
            
        
    

def login() :
    
    while True :
        print("1.VIEW PATIENT DETAILS")
        print("2.VIEW DOCTOR DETAILS")
        print("3.BOOK APPOINTMENT")
        print("4.EXIT")
        ch=int(input("Enter choice :"))
        if ch==1 :
            pid=int(input("Enter patient id :"))
            cur=conn.cursor()
            cur.execute("SELECT*FROM PATIENTDETAILS WHERE PATIENTID={}".format(pid))
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
                
        elif ch==2 :
            Y = PrettyTable()
            cur = conn.cursor()
            cur.execute("SELECT*FROM DOCTOR_DETAILS")
            Y = from_db_cursor(cur)
            print("\nPATIENT DETAILS :\n")
            print(Y)
        elif ch==3 :
            BOOKEDAPPOINTMENTPT.book()
        elif ch==4 :
            print("THANK YOU")
            break
        else :
            print("PLEASE ENTER VALID CHOICE!")

def register() :
    while True :
        
        print("1.INSERT DETAILS(IF DOESNT EXIST)")
        print("2.VIEW PATIENT DETAILS")
        print("3.VIEW DOCTOR DETAILS")
        print("4.BOOK APPOINTMENT")
        print("5.EXIT")
        ch=int(input("Enter choice :"))
        if ch==1 :
            PATIENTPT.insert()
        elif ch==2 :
            cur=conn.cursor()
            pid=int(input("Enter patient id :"))
            cur.execute("SELECT*FROM PATIENTDETAILS WHERE PATIENTID={}".format(pid))
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
                
        elif ch==3 :
            Y = PrettyTable()
            cur = conn.cursor()
            cur.execute("SELECT*FROM DOCTOR_DETAILS")
            Y = from_db_cursor(cur)
            print("\nPATIENT DETAILS :\n")
            print(Y)
        elif ch==4 :
            BOOKEDAPPOINTMENTPT.book()
        else :
            break
    
        
        
    
def mainadmin() :
    while True :
        print("\nTABLES TO PERFORM OPERATIONS ON :\n")
        print("1.PATIENT TABLE")
        print("2.DOCTOR TABLE")
        print("3.NURSE TABLE")
        print("4.APPOINTMENT TABLE")
        print("5.BOOKED APPOINTMENTS TABLE")
        print("6.EXIT")
        ch=int(input("Enter choice :"))
        if ch==1 :
            patientadmin()
        elif ch==2 :
            doctortable()
        elif ch==3 :
            nurse()
        elif ch==4 :
            appointments()
        elif ch==5 :
            bookappt()
        else :
            break

def mainuser() :
    while True :
        print("1.LOGIN")
        print("2.REGISTER")
        print("3.EXIT")
        ch=int(input("Enter choice :"))
        if ch==1 :
            login()
        elif ch==2 :
            register()
        elif ch==3 :
            print("THANK YOU!")
            break
        else :
            print("PLEASE ENTER VALID CHOICE !")
            

#MAIN PROGRAM
print("="*25)
print("SILVERWOOD MEDICAL CLINIC")
print("="*25)
while True :
    print()
    print("="*25)
    print("1. ADMINISTRATION")
    print("2. USER SIGN IN")
    print("3. USER REGISTER")
    print("4. EXIT")
    print("="*25)
    print()
    ch=int(input("Enter choice :"))
    if ch==1 :
        username=input("Enter admin username :")
        password=input("Enter admin password :")
        if username=="admin" and password=="SMC2022.12#" :
            print("ACCESS PERMITTED!")
            mainadmin()
        else :
            print("ACCESS DENIED!")
    elif ch==2 :
        cur=conn.cursor()
        user=input("Enter username :")
        pw=input("Enter password :")
        cur.execute("SELECT*FROM USERIDS WHERE USERNAME='{}'".format(user))
        row=cur.fetchall()
        #print(row)
        if row[0][1]==pw :
            print("Successful sign in")
            login()
            
        else :
            print("Incorrect username/password")

    elif ch==3 :
        username=input("Enter username to register :")
        password=input("Enter password(preferrably strong) :")
        USERIDPT.insert(username,password)
        register()
    elif ch==4 :
        print("THANK YOU")
        print("\nSILVERWOOD MEDICAL CLINIC AWAITS YOUR NEXT ENTRY!\n")
        break
    else :
        print("\nPLEASE ENTER VALID CHOICE!")
        
        
        
    
