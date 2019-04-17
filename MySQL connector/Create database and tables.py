import mysql.connector 
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "password")

mycursor = mydb.cursor()

#to create a database
#mycursor.execute("DROP DATABASE COMPAN")
mycursor.execute("CREATE DATABASE COMPANY")
mycursor.execute("USE COMPANY")

# ***To create various tables***

#to create Department table
mycursor.execute("CREATE TABLE DEPARTMENT(Dname VARCHAR(15) NOT NULL,Dnumber INT NOT NULL,Mgr_ssn CHAR(9) NOT NULL,Mgr_start_date DATE,PRIMARY KEY(Dnumber),UNIQUE(Dname))")

#to create Employee table
mycursor.execute("CREATE TABLE EMPLOYEE(Fname VARCHAR(15) NOT NULL, Mname CHAR, Lname VARCHAR(15) NOT NULL, Ssn CHAR(9) NOT NULL, Bdate DATE, Address VARCHAR(30), Sex CHAR, Salary DECIMAL(10,2), Super_ssn CHAR(9), Dno INT NOT NULL, PRIMARY KEY(Ssn), FOREIGN KEY(Super_ssn) REFERENCES EMPLOYEE(Ssn),FOREIGN KEY(Dno) REFERENCES DEPARTMENT(Dnumber))")

#add a foreign key to Department table
mycursor.execute("ALTER TABLE DEPARTMENT ADD FOREIGN KEY(Mgr_ssn) REFERENCES EMPLOYEE(Ssn)")

#to create Department locations table
mycursor.execute("CREATE TABLE DEPT_LOCATIONS(Dnumber INT NOT NULL, Dlocation VARCHAR(15) NOT NULL, PRIMARY KEY(Dnumber, Dlocation), FOREIGN KEY (Dnumber) REFERENCES DEPARTMENT (Dnumber))")

#to create Project table
mycursor.execute("CREATE TABLE PROJECT(Pname VARCHAR(15) NOT NULL, Pnumber INT NOT NULL, Plocation VARCHAR(15), Dnum INT NOT NULL, PRIMARY KEY(Pnumber), UNIQUE(Pname), FOREIGN KEY(Dnum) REFERENCES DEPARTMENT(Dnumber))")
            
#to create Works_On table
mycursor.execute("CREATE TABLE WORKS_ON(Essn CHAR(9) NOT NULL, Pno INT NOT NULL, Hours DECIMAL(3,1) NOT NULL, PRIMARY KEY (Essn, Pno), FOREIGN KEY (Essn) REFERENCES EMPLOYEE(Ssn), FOREIGN KEY (Pno) REFERENCES PROJECT(Pnumber))")

#to create Dependent table
mycursor.execute("CREATE TABLE DEPENDENT(Essn CHAR(9) NOT NULL, Dependent_name VARCHAR(15) NOT NULL, Sex CHAR, Bdate DATE, Relationship VARCHAR(8), PRIMARY KEY(Essn, Dependent_name), FOREIGN KEY (Essn) REFERENCES EMPLOYEE(Ssn))")

print("Tables successfully created")
