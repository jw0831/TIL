# update table

import mysql.connector

conn = mysql.connector.connect(
   user='Test', password='1234', host='127.0.0.1', database='mydb')

cursor = conn.cursor()

sql = '''UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M' '''
try:
   cursor.execute(sql)
   conn.commit()
except:
   conn.rollback()
   
sql = '''SELECT * from EMPLOYEE'''

cursor.execute(sql)

print(cursor.fetchall())

conn.close()