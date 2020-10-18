from tkinter import *
win = 7

if win == 1:

    window = Tk()

    window.title("윈도창 연습")
    #########################   Label
    label1 = Label(window, text = "COOKBOOK ~~Python")
    label2 = Label(window, text = "열심히", font=("궁서체", 30), fg = "blue") #fg = foreground 글자색
    label3 = Label(window, text = "Studying", bg = "magenta", width = 20, height =5, anchor = S) #bg = background 배경색
    gatsby = PhotoImage(file = "Python_day7/200.gif")
    label4 = Label(window, image = gatsby)

    label1.pack()
    label2.pack(side=BOTTOM)
    label3.pack()
    label4.pack()
    #########################   Button
    button1 = Button(window, text = "Turn Off", fg = "red", command = quit)
    button1.pack()
    redButton=Button(window, text="Red", fg="red")
    redButton.pack(side=LEFT, fill=BOTH)
    blackButton=Button(window, text="Black", fg="Black")
    blackButton.pack(side=RIGHT,fill=BOTH)
    blueButton=Button(window, text="Blue", fg="Blue")
    blueButton.pack(side=BOTTOM,fill=BOTH)
    #########################   setting

    # window.geometry("500x200")
    window.resizable(width = True, height = True)
    #########################
    window.mainloop() #반복적으로 내부에서 WHILE루프가 돌고있다고 보면된다ㅏ.

if win == 2:
    
    window = Tk()
    window.title("practice")
    btnList = [None]*3

    for i in range (0,3):
        btnList[i] = Button(window, text = "button" + str(i+1))

    for btn in btnList:
        # btn.pack(side=RIGHT)
        btn.pack(side=TOP, fill = X, padx = 10, ipady =10)
        # btn.pack(side=BOTTOM)

    window.mainloop()

if win == 3:
    window = Tk()
    window.title("Login")
    window.geometry("200x100")
    name = Label(window, text='Name')
    name.grid(row=0, column=0)
    name_value = Entry(window)
    name_value.grid(row=0,column=1)

    password = Label(window, text='Password')
    password.grid(row=1, column=0)
    password_value = Entry(window)
    password_value.grid(row=1,column=1)

    login = Button(window, text = "Login")
    login.grid(row=2, column = 0)
    # login.pack(side=BOTTOM, fill = X, padx = 10, ipady =10)

    window.mainloop()

if win == 4:
    root = Tk()
    b = 0
    for r in range(6):
        for c in range(6):
            b = b + 1
            Button(root, text = str(b), borderwidth = 1).grid(row = r, column = c)
            
    
    root.mainloop()

if win == 5: 
    from tkinter import messagebox
    def myFunc(): #pg294
        messagebox.showinfo("Login Button", "Do you really wish to Login?")
                
    top = Tk()
    top.geometry("400x250")
    name = Label(top, text="Name").place(x=30, y=50)
    email = Label(top, text="Email").place(x=30, y=90)
    password = Label(top, text="Password").place(x=30, y=130)
    button = Button(top, text="Login", command=myFunc).place(x=30,y=170)
    e1 = Entry(top).place(x=90, y=50) #place 사용하면 get 이 안된다. pack 또는 grid를 사용해야 한다.
    e2 = Entry(top).place(x=90, y=90)
    e3 = Entry(top).place(x=90, y=130)

    top.mainloop()

if win == 6:
    from tkinter import messagebox
    window = Tk()

    ##함수 선언 부분##
    def myFunc():
        if chk.get() == 0:
            messagebox.showinfo("", "체크버튼이 꺼졌어요.")
        else:
            messagebox.showinfo("", "체크버튼이 켜졌어요.")

    ##메인 코드 부분##
    chk = IntVar() #선택된 항목에서 내용을 받을수 있음. Int
    cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

    cb1.pack()

    window.mainloop()

if win == 7:
    from tkinter import *
    from tkinter import messagebox

    def myFunc():
        num1 = entry1.get()
        num2 = entry1.get()
        messagebox.showinfo("", "what to write?")

    root = Tk()
    root.title("Calculator")

    label1 = Label(root, Text="num1").grid(row=0, column=0)
    label2 = Label(root, Text="num2").grid(row=1, column=1)

    entry1 = Entry(root).grid(row=0, column=1)
    entry2 = Entry(root).grid(row=1, column=1)

    button = Button(root, text="Calculate", command = myfunc).grid(row=3,column = 0)
    root.mainloop()

