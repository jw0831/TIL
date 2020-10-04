#관계형 데이터
#Tkinter 안에 프레임 만들기
#프레임을 만들어서 Tk() 를 올린다.

import sqlite3
from tkinter import *
from tkinter import messagebox

def userAdd():
    try:
        conn = sqlite3.connect("c:\\sqlite\\test2.db")
        sql = "INSERT INTO user VALUES (%s, '%s')" % (id.get(), name.get())
        print(sql)
        conn.execute(sql)
        conn.commit()# commint 이 위치에 있는것이 옳다!
        messagebox.showinfo("insert", "insert successfully!!!")
    except Exception as e:
        print(e)
    finally:
        conn.close()

def userUpdate():
    try:
        conn = sqlite3.connect("c:\\sqlite\\test2.db")
        sql = "UPDATE user SET name = '%s' where ID = %s" % (name.get(), id.get())
        print(sql)
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo("Update", "Update successfully!!!")
    except Exception as e:
        print(e)
    finally:
        conn.close()
def userDelete():
    try:
        conn = sqlite3.connect("c:\\sqlite\\test2.db")
        sql = "DELETE from user WHERE id = %s" % id.get()
        print(sql)
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo("delete", "delete successfully!!!")
    except Exception as e:
        print(e)
    finally:
        conn.close()
def userSelect():
    try:
        conn = sqlite3.connect("c:\\sqlite\\test2.db")
        sql = "SELECT id, name FROM user"
        print(sql)
        cursor = conn.execute(sql)
        users = cursor.fetchall() #fetchone() 할경우 루프를 돌려주면 된다잉~!
        # print(users)
        
        for user in users:
            print(user) #하게되면 새로로 볼수있음
            height = len(users) #행에 나온 갯수만큼 하려면~
            #[(1, '홍길동'),(2,'이순신'),...] => len 을 찾아서 집어넣으면 행에 나온 갯수만큼 자동으로 가능
            width = len(users[0]) #list tuple 만들 갯수만큼
            for i in range(0,height):
                for j in range(0,width):
                    print(i,j)
                    # Entry(bottom).grid(row=i, column=j)
                    b = Entry(bottom)
                    b.insert(0, users[i][j]) #0은 디폴트로 생각 / 현재 user는 리스트의 튜플 2차원 배열임
                    #a =[(1, '홍길동'),(2,'이순신'),...]
                    #일경우 a[0][0] = 1 / a[0][1] = 홍길동
                    #a[1][0], a[1][1] = 2, '이순신'        
                    b.grid(row=i, column=j)
    except Exception as e:
        print(e)
    finally:
        conn.close()

##########################################################################

master = Tk()
master.title("회원관리")
# master.geometry("300x200")
id = StringVar()
name = StringVar()
##########################################################################
#위젯화 
top = Frame(master, bg='yellow') #프레임을 만듦. 부모프레임에 붙임 
top.pack() #widget 이 되어버려서 pack 을 해주어야함
bottom = Frame(master, bg='purple')
bottom.pack() 

#구구단 처럼 밑에 그리드 셀을 만들자 5*2

# height = 5 #행에 나온 갯수만큼 하려면~
# #[(1, '홍길동'),(2,'이순신'),...] => len 을 찾아서 집어넣으면 행에 나온 갯수만큼 자동으로 가능
# #def select로 옮김
# width = 2
# for i in range(0,5):
#     for j in range(0,2):
#         Entry(bottom).grid(row=i, column=j)
##########################################################################
lbl_id=Label(top, text="ID :",bg='yellow').grid(row=0, column=0)
txt_id=Entry(top,textvariable=id).grid(row=0, column=1, columnspan=3)
lbl_name=Label(top, text="Name :",bg='yellow').grid(row=1, column=0)
txt_name=Entry(top,textvariable=name).grid(row=1, column=1, columnspan=3)
btn_add = Button(top, text="추가", fg='blue', command=userAdd).grid(row=2, column=0,sticky=W,ipadx=10)
btn_update = Button(top, text="수정", fg='blue', command=userUpdate).grid(row=2,column=1,sticky=W,ipadx=10)
btn_delete = Button(top, text="삭제", fg='blue', command=userDelete).grid(row=2,column=2,sticky=W,ipadx=10)
btn_list = Button(top, text="검색", fg='blue', command=userSelect).grid(row=2,column=3,sticky=W,ipadx=10)
master.mainloop()