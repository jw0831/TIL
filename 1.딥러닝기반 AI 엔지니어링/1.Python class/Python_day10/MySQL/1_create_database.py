# create database

import mysql.connector

conn = mysql.connector.connect(user='Test', password='1234', host='127.0.0.1')
cursor = conn.cursor()

cursor.execute("DROP database IF EXISTS MyDatabase")

sql = "CREATE database mydb";

cursor.execute(sql)

print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

conn.close()