run = 4
if run == 1:
    from tkinter import *

    def myfunc():
        print(input.get())
    window = Tk()
    input = StringVar()
    label1 = Label(window, text="ID").grid(row=0, column=0) #ID
    entry1 = Entry(window, textvariable=input).grid(row=0, column=1) #text ir
    button1 = Button(window, text="Copy", command=myfunc).grid(row=1,column = 0)

    window.mainloop()

if run == 2: #체크 박스 validation
    from tkinter import *
    from tkinter import messagebox
    window = Tk()
    ######################## function ############################
    def checkValidate():
        if check.get() == 0:
            messagebox.showerror("로그인 체크", "로그인 에러입니다. 다시 확인해주세요")
        #validation(id, password, remember)
        if check.get() == 1:
            messagebox.showinfo("로그인", "로그인 승인")


    check=IntVar()

    window.geometry("250x80")
    #Login Form using grid
   

    lblUserId = Label(window, text="아이디 :").grid(row = 0, column = 0)
    txtUserId = Entry(window).grid(row = 0, column = 1)
    lblPassword = Label(window, text="암호 :").grid(row = 1, column = 0)
    txtPassword = Entry(window).grid(row = 1, column = 1)
    ########################## Button #############################
    btnLogin = Button(window, text="로그인", command=checkValidate).grid(row = 2, column = 0)
    chckRemember = Checkbutton(window, variable=check).grid(row = 2, column = 1)

    window.mainloop()

if run == 3: #id 값 받기 / 안받으면 에러 메시지 haven't done yet
    from tkinter import *
    from tkinter import messagebox
    window = Tk()
    ######################## function ############################
    def checkValidate():
        if check.get() == 0:
            messagebox.showerror("로그인 체크", "로그인 에러입니다. 다시 확인해주세요")
        #validation(id, password, remember)
        if check.get() == 1:
            messagebox.showinfo("로그인", "로그인 승인")


    check=IntVar()

    window.geometry("250x80")
    #Login Form using grid
   

    lblUserId = Label(window, text="아이디 :").grid(row = 0, column = 0)
    txtUserId = Entry(window).grid(row = 0, column = 1)
    lblPassword = Label(window, text="암호 :").grid(row = 1, column = 0)
    txtPassword = Entry(window).grid(row = 1, column = 1)
    ########################## Button #############################
    btnLogin = Button(window, text="로그인", command=checkValidate).grid(row = 2, column = 0)
    chckRemember = Checkbutton(window, variable=check).grid(row = 2, column = 1)

    window.mainloop()

if run == 4: #validation(id, password, remember) teacher's answer
    from tkinter import *
    from tkinter import messagebox
    window = Tk()
    ######################## function ############################
    def checkValidate():
        print(userid.get(), password.get(), remember.get())
        if userid.get() and password.get() and remember.get():
            messagebox.showinfo("Login","Accept")
        else:    
            messagebox.showerror("ID", "Please fill in")    
        # messagebox.showinfo("로그인", "로그인 승인")


    window.title("로그인 화면")
    window.geometry("250x80")
    #Login Form using grid
   
    userid = StringVar()
    password = StringVar()
    remember = IntVar()

    lblUserId = Label(window, text="아이디 :").grid(row = 0, column = 0)
    txtUserId = Entry(window, textvariable=userid).grid(row = 0, column = 1)
    lblPassword = Label(window, text="암호 :").grid(row = 1, column = 0)
    txtPassword = Entry(window, textvariable=password).grid(row = 1, column = 1)
    ########################## Button #############################
    btnLogin = Button(window, text="로그인", command=checkValidate).grid(row = 2, column = 0)
    chckRemember = Checkbutton(window, variable=remember).grid(row = 2, column = 1)

    window.mainloop()

#C:\Python37\Lib\tkinter 에서 확인가능