# Computer Sciece Project (Job Portal Management)

# To Write a Program to Connect MySQL and Python to Create a Database for Job Applications 

''' 

Installing Modules  #The following modules are to be installed before using the 
program

pip install mysql.connector
pip install pymysql

'''


'''

Creating Database and Table

create database me;
use me;

create table Applicant(Aadharno varchar(20) Primary Key,
                       Name varchar(30),
                       Age int,
                       Gender varchar(1),
                       Email varchar(45),
                       Phoneno varchar(15),
                       Company varchar(30));
                       
insert into Applicant values('515105412121','Vishal Mitter',25,'M','vishalmitter2@gmail.com','1254256415','Null');
insert into Applicant values('415211482152','Mira Sulabha',24,'F','morasulabha@gmail.com','41654655165','Null');
insert into Applicant values('412165415643','Kalyani Preeti',25,'F','preetikalyani@yahoo.com','85496551667','Null');
insert into Applicant values('396872161212','Devika Kishor',26,'F',devikakishor6@gmail.com','54558555582','Null');

create table Employer(CompanyName varchar(35) Primary Key,
                      Address varchar(100),
                      Category varchar(20),
                      ContactInfo int);
                      
insert into Employer values('Artic Wolf Networks.','29, Takshila Apt, MC Road, Opp Model Town, Andheri(west), Mumbai, Maharashtra','Network Engineer',4635645103);
insert into Employer values('Eco Focus.','49/1 supreme indestatep, Pune, Maharashtra','Web Developer',16415115322);
insert into Employer values('Candor Corp.','W-318, Ttc Indl.area, Konkan Bhavan, Mumbai, Maharashtra','IT Security',44165146536);

'''



#PYTHON CODE:-

# Importing Modules/Libraries

import pymysql as ps
import smtplib

try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Use TLS to add security 
    smtp.starttls() 

    #User Authentication 
    smtp.login("school.team1234@gmail.com","CapitalC")
    
except Exception as ex: 
    print("Something went wrong...",ex)
    
def mail(Aname,Mail,Cname="F"):
    if Cname=="F":
            
            msg = """To: {} {}
MIME-Version: 1.0
Content-type: text/html
Subject: Registration successful

Congratulations {} your account has been registered.

""".format(Aname,Mail,Aname) 
    else:
            
            msg = """From: {}
To: {} {}
MIME-Version: 1.0
Content-type: text/html
Subject: Job Application Approved

Congratulations {} your application has been approved by {}
""".format(Cname,Aname,Mail,Aname,Cname)    
    #Sending the Email
    smtp.sendmail("school.team1234@gmail.com", Mail,msg)    


#Preparing the authentication process
import getpass
creds={"Mohit":"Tiwari","Piyush":"Ranjan"}
def Ck_Cd():
    while True:
        acc=input("Enter Your Username: ") 
        p = getpass.getpass(prompt='Enter your Password: ') 
        try:
            p == creds[acc]
            print('Welcome..!!!')
            p2=input("Press Enter to continue...")
            break
            
        except:
            print('The Username/Password entered by YOU is incorrect!')
            p2=input("Press Enter to continue...")        


#Main Menu
print("""
------------------------------------------------------------------------------                                                                     
                                                                            """)
print("""
             -------------------------------------------------------
             =======================================================
             ===============WELCOME TO JOB PORTAL=================
             =======================================================
             -------------------------------------------------------                                                     
                                                                     """)
                                                                        
    
print("""
________________________________________    

    | 1 |   For Applicant Section      
    ------------------------------------------
    | 2 |   For Employer Section     
    ------------------------------------------
________________________________________                                  
                                                                   """)

ch=int(input("\nEnter your Choice : "))
print("""
------------------------------------------------------------------------------                                                                     
                                                                            """)


#Applicant Portal
if ch==1:

    ch=input("Are you a new User? Y/N ")
    
    #Check New User
    if ch.capitalize()=="Y":
        user=input("Enter your User Name: ")
        p = getpass.getpass(prompt='Enter your Password: ')
        creds[user]=p
        print("Your account has been created.")
    Ck_Cd()
        
    
    while True:
        print("""
------------------------------------------------------------------------------                                                                     
                                                                            """)
        print("""
             =======================================================
             ========** Welcome to the Applicant Section **=========
             =======================================================                                                     
                                                                     """)
                                                                        
    
        print("""
________________________________________    

    | 1 |   For New Registration     
    ------------------------------------------
    | 2 |   Modify Current Registration Data     
    ------------------------------------------
    | 3 |   Browse Through Available Employers  
    ------------------------------------------
    | 4 |   Exit Program
    ------------------------------------------
________________________________________                                  
                                                                   """)
        ch=int(input("Enter your Choice :-- "))
        print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
        
    #Internal Sections
    
        #New Registration
        
        if ch==1:
            Aadhar=int(input("Enter your Aadhar No.:"))
            Aname=input("Enter your Name:")
            Aage=int(input("Enter your Age:"))
            Gen=input("Enter your Gender (M/F):")
            Mail=input("Enter your Email Address:")
            Phone=int(input("Enter your Phone No."))
            mycon=ps.connect(host="localhost", user="root", password="", database="me")
            cur=mycon.cursor()
            cur.execute("insert into Applicant values ('{}','{}','{}','{}','{}','{}','{}')".format(Aadhar,Aname,Aage,Gen,Mail,Phone,'Null'))
            mycon.commit()
            cur.execute("select Aadharno,Name,Age,Gender,Email,Phoneno from Applicant where Aadharno='{}' ".format(Aadhar))
            k=cur.fetchall()
            print("You have been successfully registered....")
            print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
            for row in k:
                for j in row:
                    print(j,end='\n')
            mycon.close()
            mail(Aname,Mail)
            print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
        
        #Modify the Applicant Data
        
        if ch==2:
            Adh=input("Enter Applicant Aadhar No.:")
            mycon=ps.connect(host="localhost", user="root", password="", database="Piyush")
            cur=mycon.cursor()
            cur.execute("select * from Applicant where Aadharno='{}' ".format(Adh))
            k=cur.fetchall()
            for row in k:
                if row[0]==Adh:
                    cur.execute("select * from Applicant where Aadharno='{}' ".format(Adh))
                    m=cur.fetchall()
                    print("You are registered under:")
                    for row in k:
                        for j in row:
                            print(j,end='\n')
                    print("Enter new Credentials: ")
                    Aname=input("Enter your Name: ")
                    Aage=int(input("Enter your Age: "))
                    Gen=input("Enter your Gender (M/F): ")
                    Mail=input("Enter your Email Address: ")
                    Phone=int(input("Enter your Phone No. "))
                    cur=mycon.cursor()
                    cur.execute("update Applicant set Name='{}',Age='{}',Gender='{}',Email='{}',Phoneno='{}' where Aadharno='{}'".format(Aname,Aage,Gen,Mail,Phone,Adh))
                    mycon.commit()
                    cur.execute("select Aadharno,Name,Age,Gender,Email,Phoneno from Applicant where Aadharno='{}' ".format(Adh))
                    k=cur.fetchall()
                    print("Your Credentials have been successfully Updated....")
                    for row in k:
                        for j in row:
                            print(j,end='\n')
                    mycon.close()
                    print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
        
        #Browse Employer List
        
        if ch==3:
            print("---Welcome to the Browse Section---")
            Adh=input("Enter your Aadhar no. to continue:")
            print("These are the Categories you can choose from: \n\t 1) Web Developer \n\t 2) Computer Systems Analyst \n\t 3) IT Security \n\t 4) Network Engineer")
            ch=int(input("Enter your choice:--"))
            if ch==1:
                cat="Web Developer"
            elif ch==2:
                cat="Computer Systems Analyst"
            elif ch==3:
                cat="IT Security"
            elif ch==4:
                cat="Network Engineer"
            else:
                print("Enter valid category no.")
            mycon=ps.connect(host="localhost", user="root", password="", database="me")
            cur=mycon.cursor()
            cur.execute("select * from Employer where Category='{}'".format(cat))
            k=cur.fetchall()
            print("number of companies under this category:",len(k))
            for row in k:
                for j in row:
                    print(j,end='\t')
            com=input("\nEnter the Company you wish to apply to:")
            mycon=ps.connect(host="localhost", user="root", password="", database="me")
            cur=mycon.cursor()
            cur.execute("select * from Employer where CompanyName='{}' ".format(com))
            k=cur.fetchall()
            for row in k:
                if row[0]==com:
                    cur.execute("update Applicant set Company='{}' where Aadharno='{}' ".format(com,Adh))
                    mycon.commit()
                    m=cur.fetchall() 
                    print("You have successfully applied for",com)
            mycon.close()
            print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")

        #Quit
        if ch==4:
            print("Press Enter to exit. ")
            break
        


#Employer Portal        
if ch==2:
    
    ch=input("Are you a new User? Y/N ")
    
    #Check New User
    if ch.capitalize()=="Y":
        user=input("Enter your user name: ")
        p = getpass.getpass(prompt='Enter your Password: ')
        creds[user]=p
        print("Your a/c has been created")
    Ck_Cd()

    while True:
        print("""
             =======================================================
             ========** Welcome to the Employer Section **=========
             =======================================================                                                     
                                                                     """)
                                                                        
    
        print("""
________________________________________    

    | 1 |   For New Registration     
    ------------------------------------------
    | 2 |   Modify Current Registration Data     
    ------------------------------------------
    | 3 |   Browse Through Applicant List
    ------------------------------------------
    | 4 |   Exit Program
    ------------------------------------------
________________________________________                                  
                                                                   """)
        ch=int(input("Enter your Choice :-- "))
        print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
    #Internal Sections

        #New Registration
        
        if ch==1:
            Cname=input("Enter your Company Name: ")
            Add=input("Enter Company Address: ")
            Mail=input("Enter Applicant Category: ")
            Cont=int(input("Enter your Contact Info: "))
            mycon=ps.connect(host="localhost", user="root", password="", database="me")
            cur=mycon.cursor()
            cur.execute("insert into Employer values ('{}','{}','{}','{}')".format(Cname,Add,Mail,Cont))
            mycon.commit()
            cur.execute("select * from Employer where CompanyName='{}' ".format(Cname))
            k=cur.fetchall()
            print("Your Company has been successfully registered....")
            print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
            for row in k:
                for j in row:
                    print(j,end='\n')
            mycon.close()
            print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
        
        #Modify the Employer Data
        
        if ch==2:
            Com=input("Enter Company Name: ")
            mycon=ps.connect(host="localhost", user="root", password="", database="me")
            cur=mycon.cursor()
            cur.execute("select * from Employer where CompanyName='{}' ".format(Com))
            k=cur.fetchall()
            for row in k:
                if row[0]==Com:
                    cur.execute("select * from Employer where CompanyName='{}' ".format(Com))
                    m=cur.fetchall()
                    print("You are registered under: ")
                    for row in k:
                        for j in row:
                            print(j,end='\n')
                    print("Enter new Credentials: ")
                    Cname=input("Enter your Company Name: ")
                    Add=input("Enter Company Address: ")
                    Mail=input("Enter Applicant Category: ")
                    Cont=int(input("Enter your Contact Info: "))
                    cur=mycon.cursor()
                    cur.execute("update Employer set CompanyName='{}',Address='{}',Category='{}',ContactInfo='{}' where CompanyName='{}'".format(Cname,Add,Mail,Cont,Cname))
                    mycon.commit()                    
                    cur.execute("select * from Employer where CompanyName='{}' ".format(Com))
                    print("Your Credentials have been successfully Updated....")
                    k=cur.fetchall()
                    for row in k:
                        for j in row:
                            print(j,end='\n')
                    mycon.close()
                    print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
        
        #Browse Applicant List
        
        
        if ch==3:
            print("Welcome to your Company's Browse Section")
            Com=input("Enter Company Name: ")
            print("You can go through the list of interested applicants for your company....")
            print("The list of interested applicants is - ")
            mycon=ps.connect(host="localhost", user="root", password="", database="me")
            cur=mycon.cursor()
            cur.execute("select Aadharno,Name,Age,Gender,Email,Phoneno from Applicant where Company='{}'".format(Com))
            k=cur.fetchall()
            for row in k:
                for j in row:
                    print(j,end='\t')
            Add=input("\nEnter the Aadharno of the Applicant you choose to select: ")
            for row in k:
                if row[0]==Add:
                    print("You have chosen",row[1]," for your Company. ")
                    mail(row[1],row[4],Com)
            print("""\n
------------------------------------------------------------------------------    
                                                                            \n""")
                    
        #Quit
        if ch==4:
            
            break
ch=input("Press Enter to exit. ")
        


