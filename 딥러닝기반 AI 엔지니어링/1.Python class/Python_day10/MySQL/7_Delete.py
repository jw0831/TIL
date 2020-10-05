# delete table

import mysql.connector

conn = mysql.connector.connect(user='Test', password='1234', host='127.0.0.1', database='mydb')

cursor = conn.cursor()

print("Contents of the table: ")
cursor.execute("SELECT * from EMPLOYEE")
print(cursor.fetchall())

sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (25)

try:
   cursor.execute(sql)
   conn.commit()
except:
   conn.rollback()

print("Contents of the table after delete operation ")
cursor.execute("SELECT * from EMPLOYEE")
print(cursor.fetchall())

conn.close()