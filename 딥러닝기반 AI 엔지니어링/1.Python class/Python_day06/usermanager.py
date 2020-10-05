import os
import io
import time

class UserManager:	
	def getUsers(self):		
		self.f = open("users.txt", 'r', encoding='utf-8')
		self.lines = self.f.readlines()
		for self.line in self.lines:
			print(self.line.replace("\n",""))
		self.f.close()
	def getUserByName(self, name):		
		self.user = name
		self.f = open('users.txt', 'r', encoding='utf-8')
		self.lines = self.f.readlines()
		self.check = False
		self.user2 = ''
		for self.line in self.lines:
			# "홍길동\n" == "홍길동"
			self.line = self.line.replace("\n","")
			if self.line == self.user:
				self.user2 = self.line
				self.check = True
				break
		if self.check:
			print("회원은 존재합니다. : %s" % self.user2)
		else:
			print("회원은 존재하지 않습니다. : %s" % self.user)
	def createUser(self, name):
		self.user = name
		if os.path.exists("users.txt"):
			self.f = open("users.txt", "r", encoding="utf-8")
			self.lines = self.f.readlines()
			self.f.close()
			self.f = open("users.txt", "w", encoding='utf-8')
			for self.line in self.lines:
				self.f.write(self.line)		
			self.f.write(self.user + "\n")
			self.f.close()
			print("회원을 추가하였습니다.")
		else:			
			self.f = open("users.txt", "w", encoding="utf-8")
			self.f.write(self.user + "\n")
			self.f.close()
			print("users.txt파일이 없어서 파일을 생성하고 회원을 추가하였습니다.")
	def updateUser(self, name, new_name):
		self.user = name
		self.new_name = new_name
		self.f = open("users.txt", 'r', encoding='utf-8')
		self.lines = self.f.readlines()		
		self.f.close()
		self.f = open("users.txt", 'w', encoding="utf-8")
		for self.line in self.lines:
			self.line = self.line.replace("\n","")			
			if self.line == self.user: 
				self.line = self.new_name				
			self.f.write(self.line + "\n")
		self.f.close()	
	def deleteUser(self, name):
		self.user = name
		self.f = open("users.txt", 'r', encoding='utf-8')
		self.lines = self.f.readlines()
		self.f.close()
		self.f = open("users.txt", 'w', encoding="utf-8")
		for self.line in self.lines:
			self.line = self.line.replace("\n","")
			if self.line == self.user: continue
			self.f.write(self.line + "\n")
		self.f.close()	

class AppManager:
	
	def run(self):
		self.userMgr = UserManager()

		while True:
			print("# 회원관리 ")
			print("#########################")
			print(" 1. 전체회원검색")
			print(" 2. 회원검색")
			print(" 3. 회원추가")
			print(" 4. 회원수정")
			print(" 5. 회원삭제")
			print(" 6. 종료")
			print("#########################")
			sel = input("메뉴를 선택해주세요.(1-6): ")
			if sel == "1":
				self.userMgr.getUsers()
				time.sleep(2)
			elif sel == "2":
				self.name = input("회원명을 입력해주세요. : ")
				self.userMgr.getUserByName(self.name)
				time.sleep(2)
			elif sel == "3":
				self.name = input("회원명을 입력해주세요. : ")
				self.userMgr.createUser(self.name)
				time.sleep(2)
			elif sel == "4":
				self.name = input("회원명을 입력해주세요. : ")
				self.new_name = input("새회원명을 입력해주세요. : ")
				self.userMgr.updateUser(self.name, self.new_name)
				time.sleep(2)
			elif sel == "5":
				self.name = input("회원명을 입력해주세요. : ")
				self.userMgr.deleteUser(self.name)
				time.sleep(2)
			elif sel == "6":
				print("감사합니다. 수고하십시요.")				
				time.sleep(2)
				break
			else:
				print("잘못입력하셨습니다. 다시 확인 부탁드립니다.")
				time.sleep(2)
				break

if __name__ == "__main__":
	app = AppManager()
	app.run()

#class User:
#	def __init__(self, name=''):
#		self.__name = name
#	def getName(self):
#		return self.__name
#	def setName(self, name):
#		self.__name = name