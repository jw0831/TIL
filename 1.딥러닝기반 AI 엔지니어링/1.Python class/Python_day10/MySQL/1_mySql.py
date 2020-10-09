'''
# select table

import mysql.connector

conn = mysql.connector.connect(
   user='Test', password='1234', host='192.168.0.30', database='employees') #이 정보를 잘 넣어주어야 처리가 된다...

cursor = conn.cursor()

sql = 'SELECT * from employees.employees'

cursor.execute(sql)

result = cursor.fetchone();
print(result) #(10001, datetime.date(1953, 9, 2), 'Georgi', 'Facello', 'M', datetime.date(1986, 6, 26))

# result = cursor.fetchall();
# print(result) #(10001, datetime.date(1953, 9, 2), 'Georgi', 'Facello', 'M', datetime.date(1986, 6, 26)).................................

conn.close()
'''

# # select table

# import mysql.connector

# conn = mysql.connector.connect(
#    user='Test', password='1234', host='192.168.0.30', database='employees') #이 정보를 잘 넣어주어야 처리가 된다...

# cursor = conn.cursor()

# sql = 'SELECT * FROM employees.employees WHERE emp_no = %s'

# cursor.execute(sql, (10001,)) #comma 를 넣어주어야함 

# # result = cursor.fetchone();
# # print(result) #(10001, datetime.date(1953, 9, 2), 'Georgi', 'Facello', 'M', datetime.date(1986, 6, 26))

# result = cursor.fetchall();
# print(result) #(10001, datetime.date(1953, 9, 2), 'Georgi', 'Facello', 'M', datetime.date(1986, 6, 26)).................................

# conn.close()

# select table

import mysql.connector
emp_no = 10001
conn = mysql.connector.connect(
   user='Test', password='1234', host='192.168.0.30', database='employees') #이 정보를 잘 넣어주어야 처리가 된다...

cursor = conn.cursor()

sql = 'SELECT * FROM employees.employees WHERE emp_no = %s'

cursor.execute(sql, (emp_no,)) #comma 를 넣어주어야함 

# result = cursor.fetchone();
# print(result) #(10001, datetime.date(1953, 9, 2), 'Georgi', 'Facello', 'M', datetime.date(1986, 6, 26))

result = cursor.fetchall();
print(result) #(10001, datetime.date(1953, 9, 2), 'Georgi', 'Facello', 'M', datetime.date(1986, 6, 26)).................................

conn.close()

# # where 

# import mysql.connector

# conn = mysql.connector.connect(
#    user='Test', password='1234', host='192.168.0.30', database='employees')

# cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# sql = CREATE TABLE EMPLOYEE(
#    FIRST_NAME CHAR(20) NOT NULL,
#    LAST_NAME CHAR(20),
#    AGE INT,
#    SEX CHAR(1),
#    INCOME FLOAT
# )'''
# cursor.execute(sql)

# insert_stmt = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
#    VALUES (%s, %s, %s, %s, %s)"

# data = [('John', 'Lee', 19, 'M', 2000), ('Tom', 'Lee', 20, 'M', 7000),
# ('Amy', 'Steve', 25, 'F', 5000),('Gary', 'Tomson', 26, 'M', 2000)]
# cursor.executemany(insert_stmt, data)
# conn.commit()

# cursor.execute("SELECT * from EMPLOYEE WHERE AGE <23")
# print(cursor.fetchall())

# conn.close()

