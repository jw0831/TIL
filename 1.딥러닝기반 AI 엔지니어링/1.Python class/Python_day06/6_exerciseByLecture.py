#깃허브에 있는 좋은 코드들을 프린트해서 이해하면서 구조를 보면 실력이 늘어요호호

# class 사용할때 인스턴스 변수를 사용하는게 훨씬 better
import os
import io
import time

class UserManager:
    def getUsers(self):
        self.f = open("users.txt", "r", encoding = 'utf-8')
        self.lines = self.f.readlines()
        print(self.lines)
        for self.line in self.lines:
            print(self.line.replace("\n",""))
        self.f.close()
    def getUserByName(self, name):
        pass
    def createUser(self, name):
        pass
    def updateUser(self, name, new_name):
        pass
    def deleteUser(self, name):
        pass
    # continue 를 사용해서 (바이파스도 하고) 더이상 쓰지 못하도록함

class AppManager:
    def run(self):
        self.userMgr = UserManager() #instance variable
        while True:
            print("#회원관리")
            print("#########################")
            print(" 1. 전체회원검색")
            print(" 2. 회원검색")
            print(" 3. 회원추가")
            print(" 4. 회원수정")
            print(" 5. 회원삭제")
            print(" 6. 종료")
            print("#########################")
            sel = input("메뉴를 선택해주세요 (1-6) : ")
            if sel == "1":
                self.userMgr.getUsers()

            elif sel == "2":
                pass
            elif sel == "3":
                pass
            elif sel == "4":
                pass
            elif sel == "5":
                pass
            elif sel == "6":
                print("end")
                break
            else:
                print("wrong input")

if __name__ = "__main__":
    app = AppManager()
    app.run()



