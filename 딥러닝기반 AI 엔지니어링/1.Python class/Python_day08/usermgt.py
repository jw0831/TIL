import sqlite3
from tkinter import *
from tkinter import messagebox

def userAdd():	
	try:
		conn = sqlite3.connect("c:\\sqlite\\test2.db")
		sql = "insert into user values(%s,'%s')" % (id.get(), name.get())
		print(sql)
		conn.execute(sql)
		messagebox.showinfo("insert", "insert successfully!!!")
	except Exception as e:
		print(e) #여기서 예외처리를 해줌으로써 오류를 보여주고 finally를 사용해서 프로그램이 계속 작동하도록 하였음.
	finally:	
		conn.commit()
		conn.close()
def userUpdate():
	try:
		conn = sqlite3.connect("c:\\sqlite\\test2.db")
		sql = "update user set name = '%s' where id = %s" % (name.get(), id.get())
		print(sql)	
		conn.execute(sql)
		messagebox.showinfo("update", "update successfully!!!")
	except Exception as e:
		print(e)
	finally:				
		conn.commit()
		conn.close()
def userDelete():
	try:
		conn = sqlite3.connect("c:\\sqlite\\test2.db")
		sql = "delete from user where id = %s" % id.get()
		print(sql)
		conn.execute(sql)
		messagebox.showinfo("delete", "delete successfully!!!")
	except Exception as e:
		print(e)
	finally:	
		conn.commit()
		conn.close()

def userSelect():
	try:
		conn = sqlite3.connect("c:\\sqlite\\test2.db")
		sql = "select id, name from user"
		print(sql)
		cursor = conn.execute(sql)
		users = cursor.fetchall()	
		print(users)
	except Exception as e:
		print(e)
	finally:
		conn.close()

master = Tk()
master.title("회원관리")
master.geometry("240x80")
id = StringVar()
name = StringVar()
lbl_id = Label(master, text="아이디").grid(row=0,column=0)
txt_id = Entry(master, textvariable=id).grid(row=0,column=1,columnspan=3)
lbl_name = Label(master, text="이름").grid(row=1,column=0)
txt_name = Entry(master, textvariable=name).grid(row=1,column=1,columnspan=3)
btn_add = Button(master, text="추가",command=userAdd).grid(row=2,column=0,sticky=W)
btn_update = Button(master, text="수정", command=userUpdate).grid(row=2,column=1,sticky=W)
btn_delete = Button(master, text="삭제", command=userDelete).grid(row=2,column=2,sticky=W)
btn_list = Button(master, text="검색", command=userSelect).grid(row=2,column=3,sticky=W)

master.mainloop()