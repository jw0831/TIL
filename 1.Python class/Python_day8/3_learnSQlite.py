'''
#https://www.sqlite.org/index.html 
path 추가 해주기

sqlite>SELECT * from COMPANY where AGE>= 25 AND SALAYRI=66000

select NAME. ID from COMPANY    

select*from COMPANY where ID == 1;

NOT NULL : 무조건 값이 들어가야 한다!
'''
#데이터베이스 연결
# import sqlite3
# conn = sqlite3.Connection('C:\\sqlite\\user2.db')
# print("connected") #연결이 되면 connected 가 보인다.

# sql = '''CREATE TABLE COMPANY2
#         (ID INT PRIMARY KEY     NOT NULL,
#         NAME TEXT NOT NULL,
#         AGE INT NOT NULL,
#         ADDRESS CHAR(50),
#         SALARY  REAL);'''
# conn.execute(sql)
# conn.close()
# print("Successful")


# import sqlite3
# conn = sqlite3.Connection('C:\\sqlite\\user2.db')
# print("Opened database successfully")
# conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, '이순신', 32, 'California', 20000.00 )")
# conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, '강감찬', 25, 'Texas', 15000.00 )")
# conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, '홍길동’', 23, 'Norway', 20000.00 )")
# conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, '세종대왕', 25, 'Rich-Mond ', 65000.00 )")
# conn.commit() #이것을 작성해 주어야 등록이 된다.
# print("Records created successfully")
# conn.close()

#SELECT Operation

# import sqlite3
# conn = sqlite3.Connection("C:\\sqlite\\user2.db")
# print("Opened database successfully")
# cursor = conn.execute("SELECT id, name, address, salary from COMPANY2")
# for row in cursor:
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("ADDRESS = ", row[2])
#     print("SALARY = ", row[3], "\n")
# print("Operation done successfully")
# conn.close()
    
# import sqlite3
# conn = sqlite3.Connection("C:\\sqlite\\user2.db")
# print("Opened database successfully")
# conn.execute("INSERT INTO COMPANY2 (ID, NAME, AGE, ADDRESS, SALARY) VALUES (5, '이순신', 32, 'California', 200000.00)") #ID 에 같은 숫자가 들어가면 (중복되면)안되는 설정PK때문에 막힘
# conn.execute("INSERT INTO COMPANY2 (ID, NAME, AGE, ADDRESS, SALARY) VALUES (6, '강감찬', 44, 'Texas', 45000.00)")
# conn.execute("INSERT INTO COMPANY2 (ID, NAME, AGE, ADDRESS, SALARY) VALUES (7, '홍길동', 33, 'America', 200000.00)")
# conn.execute("INSERT INTO COMPANY2 (ID, NAME, AGE, ADDRESS, SALARY) VALUES (8, '세종대왕', 60, 'Rich-Mond', 65000.00)")
# conn.commit()
# print("Records created successfully")
# conn.close()

import sqlite3
from tkinter import *

master = Tk()
master.title("Enter SQLite")
id = StringVar() #여기서 받았을때 int로 해버리면 소수점이 잘려버린다. 문자 처리를 하고 및에 78번 라인에서 %s 처리를 %s 또는 '%s' 해주면 된다.
name = StringVar()
age = StringVar()
address = StringVar()
salary = StringVar()

def mySave():
    conn = sqlite3.connect("C:\\sqlite\\user2.db") #sqlite 는 connect 사용!!!
    sql = "INSERT INTO COMPANY2 VALUES (%s,'%s',%s,'%s',%s)" % (id.get(),name.get(),age.get(),address.get(),salary.get()) #문자열 parameter처리 하기 '%s' !!!
    print(sql)
    conn.execute(sql)
    conn.commit()
    print("Saved")
    conn.close()

lbl_id = Label(master, text="ID").grid(row=0, column=0)
txt_id = Entry(master, textvariable=id).grid(row=1, column=0)
lbl_name = Label(master, text="name").grid(row=0, column=1)
txt_name = Entry(master, textvariable=name).grid(row=1, column=1)
lbl_age = Label(master, text="age").grid(row=0, column=2)
txt_age = Entry(master, textvariable=age).grid(row=1, column=2)
lbl_address = Label(master, text="address").grid(row=0, column=3)
txt_address = Entry(master, textvariable=address).grid(row=1, column=3)
lbl_salary = Label(master, text="salary").grid(row=0, column=4)
txt_salary = Entry(master, textvariable=salary).grid(row=1, column=4)
btn_save = Button(master, text="Save", command=mySave).grid(row=2,column=2)

master.mainloop()