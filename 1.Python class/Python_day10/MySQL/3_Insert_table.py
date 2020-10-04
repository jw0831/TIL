# # insert table

# import mysql.connector

# conn = mysql.connector.connect(
#    user='Test', password='1234', host='127.0.0.1', database='mydb')

# cursor = conn.cursor() #MySQL 에서는 변수를 받아서 사용한다.

# sql = """INSERT INTO EMPLOYEE(
#    FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
#    VALUES ('John', 'Lee', 20, 'M', 2000)"""

# try:
#    cursor.execute(sql)
#    conn.commit()

# except:
#    conn.rollback()

# conn.close()

# 

import mysql.connector

conn = mysql.connector.connect(
   user='Test', password='1234', host='127.0.0.1', database='mydb')

cursor = conn.cursor()

insert_stmt = (
   "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
   "VALUES (%s, %s, %s, %s, %s)" # % ( , , ) 넣어도 되고 아래처럼 해도된다. 여기는 무조건 %s 
) 
data = ('John', 'Lee', 25, 'F', 5000) #tuple 에 문자열 그러므로 위에  '%s'안하고 %s 만 하면됨

try:
   cursor.execute(insert_stmt, data)
   
   conn.commit()

except:
   conn.rollback()

print("Data inserted")

conn.close()