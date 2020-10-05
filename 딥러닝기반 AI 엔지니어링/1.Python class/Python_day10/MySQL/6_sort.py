# 

import mysql.connector

conn = mysql.connector.connect(
   user='Test', password='1234', host='127.0.0.1', database='mydb')

cursor = conn.cursor()

# cursor.execute("SELECT * from EMPLOYEE ORDER BY INCOME DESC")
cursor.execute("SELECT * from EMPLOYEE ORDER BY INCOME") #default ASC

print(cursor.fetchall())

conn.close()