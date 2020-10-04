'''
# 사원관리
#########################
 1. 전체사원검색
 2. 사원검색
 3. 사원추가
 4. 사원수정
 5. 사원삭제
 6. 종료
#########################
메뉴를 선택해주세요.(1-6):

* 다음 메뉴를 구성하고 회원을 관리할수 있도록 처리한다.
- 회원추가시 중복처리를 하고, 다른 예외 상황이 생긴 경우 예외처리를 하시오.

* 데이터저장소 : sqlite
데이터베이스명 : company
테이블명 및 컬럼 
- table name : emp
- columns 
  id(아이디) : int, primary key, not null
  name(이름) : text, not null
'''

from tkinter import *
from tkinter import messagebox
import time
import sqlite3
from sqlite3 import Error
######################################################################
def searchAll():
    try:
        conn = sqlite3.connect("c:\\sqlite\\company.db")
        # print("conneted")
        sql = "SELECT id , name FROM emp"
        print(sql)
        cursor = conn.execute(sql)
        users = cursor.fetchall()
        print(users)
        for user in users:
            print(user)
            height = len(users)
            width = len(users[0])
            for i in range (0,height):
                for j in range (0, width):
                    print(i,j)
                    list = Entry(bottom)
                    list.insert(0, users[i][j])
                    list.grid(row=i, column=j)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    # print("closed")
def searchIndiv():
    try:
        conn = sqlite3.connect("c:\\sqlite\\company.db")
        sql = "SELECT id, name from emp WHERE id = %s AND name = '%s'" % (id.get(), name.get())
        print(sql)
        cursor = conn.execute(sql)
        users = cursor.fetchone()
        print(users)
        if users == None:
            print("there is no one")
            messagebox.showinfo("notice","Client do not exists or match\nTry again!")
        else:
            print("exist")
            messagebox.showinfo("notice","Client exists!!")
        conn.commit()
        # if sql:
        #     messagebox.showinfo("notice", "client exist")
        # else:
        #     messagebox.showinfo("notice", "client does not exist")
    except Exception as e:
        print(e)
        messagebox.showerror("Notice","Please fill in ID and Name")
    finally:
        conn.close()
    
def add():
    try:
        conn = sqlite3.connect("c:\\sqlite\\company.db")
        sql = "INSERT INTO emp VALUES (%s, '%s')" % (id.get(), name.get())
        print(sql)
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo("정보", "사원이 추가되었습니다.\nID: %s\nName: %s" % (id.get(), name.get())) 
    except Exception as e:
        print(e)
        # print('SQLite error: %s' % (''.join(er.args)))
        if (e == "near ",": syntax error"):
            messagebox.showerror("Error","ID 와 Name 을 입력해 주세요!")
        if (e == "UNIQUE constraint failed: emp.id"):
            messagebox.showerror("Error","ID 가 중복됩니다!!\n확인바람")
    finally:
        conn.close()
    
def update():
    try:
        conn = sqlite3.connect("c:\\sqlite\\company.db")
        sql = "UPDATE emp SET name = '%s' where ID = %s" % (name.get(), id.get())
        print(sql)
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo("notice", "ID: %s has been updated to %s" % (id.get(), name.get()))
    except Exception as e:
        print(e)
    finally:    
        conn.close()
    
def delete():
    try:
        conn = sqlite3.connect("c:\\sqlite\\company.db")
        sql = "DELETE FROM emp WHERE id = %s" % id.get()
        print(sql)
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo("notice","ID: %s has been deleted" % id.get())
    except Exception as e:
        print(e)
        messagebox.showerror("notice","Please enter the value")
    finally:
        conn.close()
    
def terminate():
    conn = sqlite3.connect("c:\\sqlite\\company.db")
    conn.close()
    exit()
######################################################################
master = Tk()
master.title("사원관리")
master.geometry("300x300")
######################################################################
id = StringVar()
name = StringVar()

top = Frame(master, bg='yellow', padx=30)
bottom = Frame(master, bg='red')
top.pack()
bottom.pack()
######################################################################
lbl_main = Label(top, text='사원관리 시스탬', bg='yellow').grid(row=0,columnspan=2)
lbl_mesg = Label(top, text='메뉴를 선택해주세요 (1-6)', bg='yellow').grid(row=1,columnspan=2)
lbl_id = Label(top, text='ID:', bg='yellow').grid(row=2,column=0)
ent_id = Entry(top, textvariable=id).grid(row=2,column=1)
lbl_name = Label(top, text='Name:', bg='yellow').grid(row=3,column=0)
ent_name = Entry(top, textvariable=name).grid(row=3,column=1)
btn_searchAll = Button(top, text="1. 전체사원검색", command=searchAll).grid(row=4,columnspan=2)
btn_searchAll = Button(top, text="2. 사원검색", command=searchIndiv).grid(row=5,columnspan=2)
btn_searchAll = Button(top, text="3. 사원추가", command=add).grid(row=6,columnspan=2)
btn_searchAll = Button(top, text="4. 사원수정", command=update).grid(row=7,columnspan=2)
btn_searchAll = Button(top, text="5. 사원삭제", command=delete).grid(row=8,columnspan=2)
btn_searchAll = Button(top, text="6. 종료", command=terminate).grid(row=9,columnspan=2)



# print("# 사원관리")
# print("#########################")
# print("1. 전체사원검색")
# print("2. 사원검색")
# print("3. 사원추가")
# print("4. 사원수정")
# print("5. 사원삭제")
# print("6. 종료")
# print("#########################")
# print("메뉴를 선택해주세요.(1-6):")

######################################################################
master.mainloop()