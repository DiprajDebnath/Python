import mysql.connector 
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "password")

mycursor = mydb.cursor()
mycursor.execute("USE COMPANY")


#'''Insert record into Employee table'''
def emp():
      sqlQuery = "INSERT INTO EMPLOYEE(Fname, Mname, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn,Dno) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

      Fname = input("Fname : ")
      Mname = input("Mname : ")
      Lname = input("Lname : ")
      Ssn = input("Ssn : ")
      Bdate = input("Bdate : ")
      Address = input("Address : ")
      Sex = input("Sex : ")
      Salary = float(input("Salary : "))
      Super_ssn = input("Super_ssn : ")
      Dno = int(input("Dno : "))
      
      values = (Fname, Mname, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno)
      mycursor.execute(sqlQuery, values)
      mydb.commit() #It commits the changes
      print(mycursor.rowcount, "record successfully inserted.\n")
      return

num = int(input("How many records you want to enter \n"))
i = 0
while(i<num):
      emp()

"""
#'''Insert record into Department table'''
sqlQuery = "INSERT INTO DEPARTMENT(Dname, Dnumber,Mgr_ssn, Mgr_start_date) VALUES (%s,%s,%s,%s)"
values = ("Research", 5,'333445555', '1988-05-22')
mycursor.execute(sqlQuery, values)
mydb.commit() #It commits the changes
print(mycursor.rowcount, "record was inserted.")
"""
