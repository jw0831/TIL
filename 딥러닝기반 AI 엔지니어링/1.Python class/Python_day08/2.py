'''
from tkinter import *
from tkinter import messagebox

master = Tk()

# def myfunc():
#     messagebox.showinfo("text", input.get())
#     print(input.get())
#     check.set(input.get()) #data가 연결이 됨 check 와

def myfunc(input, check): #lambda사용해서 할경우
    messagebox.showinfo("text", input.get())
    print(input.get())
    check.set(input.get()) #data가 연결이 됨 check 와


input = StringVar()
check = StringVar()

lbl_Label = Label(master, text="아이디").grid(row = 0, column = 0)
txt_Input = Entry(master, textvariable=input).grid(row=0, column=1)
# btn_Login = Button(master, text="로그인", command=myfunc).grid(row=1, column=0)
btn_Login = Button(master, text="로그인", command=lambda:myfunc(input,check)).grid(row=1, column=0)
lbl_Check = Checkbutton(master, text="check", textvariable = check).grid(row=1,column=1)


master.mainloop()

#이벤트 코드 pg 304  이벤트와 함수호출 및 연결
'''

from tkinter import *
from tkinter import messagebox
# pg 305
#pg309 

def keyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키: " + chr(event.keycode))

window = Tk()
window.bind("<Key>", keyEvent) #Key의 "K" 대문자임 조심 
window.mainloop()

'''
from tkinter import *

root = Tk()
def key(event):
    print("pressed", event.char)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.pack()
root.mainloop()'''

