import mysql.connector 

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "password")

mycursor.execute("CREATE TABLE DEPARTMENT(  Dname VARCHAR(15) NOT NULL,Dnumber INT NOT NULL,Mgr_ssn CHAR(9) NOT NULL,Mgr_start_date DATE,PRIMARY KEY(Dnumber),UNIQUE(Dname))")

