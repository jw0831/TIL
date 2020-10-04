## 사원관리
##########################
# 1. 전체사원검색
# 2. 사원검색
# 3. 사원추가
# 4. 사원수정
# 5. 사원삭제
# 6. 종료
##########################
#메뉴를 선택해주세요.(1-6):

#* 다음 메뉴를 구성하고 회원을 관리할수 있도록 처리한다.
#- 회원추가시 중복처리를 하고, 다른 예외 상황이 생긴 경우 예외처리를 하시오.

#* 데이터저장소 : sqlite
#데이터베이스명 : company
#테이블명 및 컬럼 
#- table name : emp
#- columns 
#  id(아이디) : int, primary key, not null
#  name(이름) : text, not null

import sqlite3
import time

class EmpManager:
	def select_emp(self):
		self.sql = "SELECT * FROM emp"
		try:
			self.conn = sqlite3.connect("c:\\sqlite\\company.db")
			self.cursor = self.conn.execute(self.sql)
			self.emps = self.cursor.fetchall()
			#print(self.emps)
		except Exception as e:
			print(e)
		finally:
			self.conn.close()
		return self.emps		
	def select_emp_id(self, id):
		self.sql = "SELECT * FROM emp where id=%s" % id
		#print(self.sql)
		try:
			self.conn = sqlite3.connect("c:\\sqlite\\company.db")
			self.cursor = self.conn.execute(self.sql)
			self.emps = self.cursor.fetchall()
			#print(self.emps)
		except Exception as e:
			print(e)		
		finally:
			self.conn.close()
		return self.emps
	def check_id(self, id):
		self.sql = "SELECT * FROM emp where id=%s" % id
		#print(self.sql)
		self.id_exists = False
		try:
			self.conn = sqlite3.connect("c:\\sqlite\\company.db")
			self.cursor = self.conn.execute(self.sql)
			if self.cursor.fetchone():
				self.id_exists = True		
			#print(self.id_exists)
		except Exception as e:
			print(e)
		finally:
			self.conn.close()
		return self.id_exists		
	def insert_emp(self, id, name):
		self.sql = "INSERT INTO emp values(%s,'%s')" % (id, name)
		#print(self.sql)
		try:
			self.conn = sqlite3.connect("c:\\sqlite\\company.db")
			self.conn.execute(self.sql)
			self.conn.commit()						
		except Exception as e:
			print(e)
		finally:
			self.conn.close()
	def update_emp(self, id, name):
		self.sql = "UPDATE emp SET name='%s' WHERE id=%s" % (name, id)
		#print(self.sql)
		try:
			self.conn = sqlite3.connect("c:\\sqlite\\company.db")
			self.conn.execute(self.sql)
			self.conn.commit()						
		except Exception as e:
			print(e)
		finally:
			self.conn.close()
	def delete_emp(self, id):
		self.sql = "DELETE FROM emp WHERE id=%s" % (id)
		#print(self.sql)
		try:
			self.conn = sqlite3.connect("c:\\sqlite\\company.db")
			self.conn.execute(self.sql)
			self.conn.commit()						
		except Exception as e:
			print(e)
		finally:
			self.conn.close()

class AppManager:
	def main(self):
		self.empmgr = EmpManager()
		while True:
			print("## 사원관리") 
			print("##########################")
			print("# 1. 전체사원검색")
			print("# 2. 사원검색")
			print("# 3. 사원추가")
			print("# 4. 사원수정")
			print("# 5. 사원삭제")
			print("# 6. 종료")
			print("##########################")
			sel = input("메뉴를 선택해주세요.(1-6):")
			if sel == "1": # 사원전체검색
				self.emps = self.empmgr.select_emp()
				for (self.id, self.name) in self.emps:
					print(self.id, self.name)
				time.sleep(2)
			elif sel == "2": # 사원아이디검색
				self.id = input("사번아이디를 입력해주세요. : ")
				self.emps = self.empmgr.select_emp_id(self.id)
				for (self.id, self.name) in self.emps:
					print(self.id, self.name)
				time.sleep(2)
			elif sel == "3": # 사원입력
				self.id = input("사번아이디를 입력해주세요. : ")
				self.name = input("이름을 입력해주세요. : ")				
				if(self.empmgr.check_id(self.id)):
					print("중복된 아이디가 존재합니다. 확인해주세요.")
				else:
					self.empmgr.insert_emp(self.id, self.name)
					print("사원이 추가되었습니다.")
				time.sleep(2)
			elif sel == "4": # 사원수정
				self.id = input("사번아이디를 입력해주세요. : ")
				self.name = input("이름을 입력해주세요. : ")
				self.empmgr.update_emp(self.id, self.name)
				print("사원정보가 수정되었습니다.")
				time.sleep(2)
			elif sel == "5": # 사원삭제
				self.id = input("사번아이디를 입력해주세요. : ")
				self.empmgr.delete_emp(self.id)
				print("해당사원이 삭제되었습니다.")
				time.sleep(2)
			elif sel == "6":
				print("감사합니다. 안녕히 가십시요.")
				time.sleep(2)
				break
			else:
				print("잘못선택하셨군요. 다시 선택해주세요.")
				time.sleep(2)
		# CRUD
		#self.empmgr.select_emp() -> table(2)
		#self.empmgr.select_emp_id(1) -> table(2)
		#self.empmgr.check_id(1) -> true or false
		#self.empmgr.insert_emp(2,'강감찬') -> None -> n affected
		#self.empmgr.update_emp(2, '홍길동') -> None -> n affected
		#self.empmgr.delete_emp(2) -> None -> n affected
		self.empmgr.select_emp()
app = AppManager()
app.main()


