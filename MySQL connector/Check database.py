#'''TO START MySQL'''
print("Welcome to MySQL")
hostName = input("Enter host name : ")
userName = input("Enter user name : ")
password = input("Enter the password : ")

import mysql.connector
mydb = mysql.connector.connect(host = hostName, user = userName, passwd = password)
mycursor = mydb.cursor()


#'''TO OPEN THE DATABASE'''
flag = 0
mycursor.execute("SHOW DATABASES")
for i in mycursor:
      if i == ('company',):
                     flag = 1
                      
if flag == 1:
      print("Database already exist")
      mycursor.execute("USE COMPANY")
      print("Tables:")
      mycursor.execute("SHOW TABLES")
      for i in mycursor:
            print(i)
else:
      print("Database does not exist")
      #createDb()	

