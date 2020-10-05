# create table

import mysql.connector

conn = mysql.connector.connect(
   user='Test', password='1234', host='127.0.0.1', database='mydb'
)

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)

conn.close()
