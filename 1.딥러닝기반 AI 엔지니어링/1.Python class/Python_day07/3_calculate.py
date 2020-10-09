from tkinter import *
from tkinter import messagebox
from functools import partial #인자를 넘길수 있는 기능이 있음

def myFunc(n1, n2):
    num1 = n1.get()
    num2 = n2.get()
    print(int(num1)+ int(num2))

root = Tk()
root.title("Calculator")
root.geometry("300x100")

number1 = StringVar()
number2 = StringVar()

label1 = Label(root, text="num1").grid(row=0, column=0)
label2 = Label(root, text="num2").grid(row=1, column=0)
entry1 = Entry(root, textvariable=number1).grid(row=0, column=1)
entry2 = Entry(root, textvariable=number2).grid(row=1, column=1)
myFunc = partial(myFunc, number1, number2)
button1 = Button(root, text="Calculate", command=myFunc).grid(row=3,column = 0)

root.mainloop()