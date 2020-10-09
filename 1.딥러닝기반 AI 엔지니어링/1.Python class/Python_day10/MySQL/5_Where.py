# where 

import mysql.connector

conn = mysql.connector.connect(
   user='Test', password='1234', host='127.0.0.1', database='mydb')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = '''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)

insert_stmt = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s, %s, %s, %s, %s)"

data = [('John', 'Lee', 19, 'M', 2000), ('Tom', 'Lee', 20, 'M', 7000),('Amy', 'Steve', 25, 'F', 5000),('Gary', 'Tomson', 26, 'M', 2000)]
cursor.executemany(insert_stmt, data) #한꺼번에 4개 싹 들어감
conn.commit()

cursor.execute("SELECT * from EMPLOYEE WHERE AGE <23")
print(cursor.fetchall())

conn.close()