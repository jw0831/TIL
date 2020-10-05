#입력, 수정, 삭제  GUI
#안되면 껐다 켜는것도 방법!!
import sqlite3
from tkinter import *
from tkinter import messagebox
conn, cur = None, None
master = Tk()
master.title("Client")
master.geometry("200x70")
######################################################################################################
id = StringVar()
name = StringVar()
######################################################################################################
def search():
    conn = sqlite3.connect("C:\\sqlite\\user2.db") #sqlite 는 connect 사용!!!
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    print("ID       name")
    print("####################")
    while (True):
        row = cur.fetchone()
        if row == None :
            break;
        data1 = row[0]
        data2 = row[1]
        if data1 == id.get() and data2 == name.get():
            print("%s '%s'" % (data1, data2))
            messagebox.showinfo("Notice", "found")
        else:
            messagebox.showinfo("Notice", "Currently there is no client") 
    messagebox.showinfo("Notice", "Done searching")
    conn.close()
    
    
    # sql = "INSERT INTO COMPANY2 VALUES (%s,'%s',%s,'%s',%s)" % (id.get(),name.get(),age.get(),address.get(),salary.get()) #문자열 parameter처리 하기 '%s' !!!
    
    
def modify():
    # conn = sqlite3.connect("C:\\sqlite\\user2.db") #sqlite 는 connect 사용!!!
    # cur = conn.cursor()
    # cur.execute()
    # messagebox.showinfo("Modifying")
    pass
def delete():
    # conn = sqlite3.connect("C:\\sqlite\\user2.db") #sqlite 는 connect 사용!!!
    # cur = conn.cursor()
    # cur.execute()
    # messagebox.showinfo("Deleting")
    pass
def add():
    # conn = sqlite3.connect("C:\\sqlite\\user2.db") #sqlite 는 connect 사용!!!
    # cur = conn.cursor()
    # cur.execute("INSERT INTO user VALUES ('%s','%s')" % (id.get(), name.get())
    # messagebox.showinfo("Including")
    pass
######################################################################################################



######################################################################################################
lbl_id = Label(master, text = "ID").grid(row=0,column=0)
txt_id = Entry(master, textvariable=id).grid(row=0,column=1,columnspan=3)
lbl_name = Label(master, text = "Name").grid(row=1,column=0)
txt_name = Entry(master, textvariable=name).grid(row=1,column=1,columnspan=3)
#--------------------------------------------------------------------#
btn_search = Button(master, text="Search", command=search).grid(row=2,column=0)
btn_modify = Button(master, text="Modify", command=modify).grid(row=2,column=1)
btn_delete = Button(master, text="Delete", command=delete).grid(row=2,column=2)
btn_add = Button(master, text="Add", command=add).grid(row=2,column=3)




######################################################################################################
master.mainloop()
