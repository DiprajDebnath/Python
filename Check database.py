
'''
hostName = input("Enter host name : ")
userName = input("Enter user name : ")
password = input("Enter the password : ")

import mysql.connector 

mydb = mysql.connector.connect(host = hostName, user = userName, passwd = password)
'''
'''Method to show tables'''
def useDb():
                mycursor.execute("USE COMPANY")
                mycursor.execute("SHOW TABLES")
                for i in mycursor:
                        print(i)


'''TO START MySQL'''
print("Welcome to MySQL")
import mysql.connector 
mydb = mysql.connector.connect(host="localhost",user="root",passwd="password")

mycursor = mydb.cursor()

if __name__ == '__main__':

        #'''TO OPEN THE DATABASE'''
        flag = 0
        mycursor.execute("SHOW DATABASES")
        for i in mycursor:
        			if i == ('company',):
        				flag = 1
    
        if flag == 1:
        	print("Database already exist")
        	useDb()
        else:
            print("Database does not exist")
            #createDb()	

