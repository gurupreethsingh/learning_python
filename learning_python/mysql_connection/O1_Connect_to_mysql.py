'''
Created on Mar 30, 2023

@author: Administrator
'''
import mysql.connector as sql

print("***************************\nConnecting to mysql from python.\n******************************* ")

myconn = sql.connect(host = "localhost" , user = "root" , passwd = "root")

if(myconn):
    print("Connection successfull")
else:
    print("Connection unsuccessfull")