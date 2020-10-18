from tkinter import *
from tkinter import messagebox

class Login:
    def __init__(self, master):
        self.master = master
        self.userid = StringVar()

        master.title = "로그인 화면"

        self.lblUserId = Label(self.master, text="아이디:").grid(row=0, column=0)        
        self.txtUserId = Entry(self.master, textvariable=self.userid).grid(row=0, column=1)
        self.btnLogin = Button(self.master, text="로그인", command=self.checkValidate).grid(row=1, column =0)

    def checkValidate(self):
        # print(self.userid.get())
        messagebox.showinfo("로그인 체크", "로그인 되었습니다.")

    # def run(self): #gui.run() 할 경우
    #     master.mainloop() #이렇게 하는 방법도 있다. 
        

        # self.master.mainloop() #도 되는데? 이건 비추 왜냐하면 생성되면서 루프가 돌아버려서 안좋음..
###########################################################
root = Tk()
gui = Login(root)
root.mainloop() #생성을 다 하고 여기서 클라스 밖에서 루프를 돌려주는게 더 안정적
# gui.run() 

# 많이 해보기!!!
# 예제도 많이... 깃헙에서 해보기
# 시험본다...
