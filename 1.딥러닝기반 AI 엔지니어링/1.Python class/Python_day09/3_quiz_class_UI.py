import sqlite3
import time

class EmpManager:
    def select_emp(self):
        self.sql = "SELECT * FROM emp"
        try:
            self.conn = sqlite3.connect("c:\\sqlite\\company.db")
            self.cursor = self.conn.execute(self.sql)
            self.emps = self.cursor.fetchall()
            # print(self.emps)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
        return self.emps

    def select_emp_id(self, id):
        self.sql = "SELECT * FROM emp where id = %s" % id
        # print(self.sql)
        try:
            self.conn = sqlite3.connect("c:\\sqlite\\company.db")
            self.cursor = self.conn.execute(self.sql)
            self.emps = self.cursor.fetchall()
            # print(self.emps)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
        return self.emps
        
    def check_id(self, id):
        self.sql = "SELECT * FROM emp where id = %s" % id
        print(self.sql)
        try:
            self.conn = sqlite3.connect("c:\\sqlite\\company.db")
            self.cursor = self.conn.execute(self.sql)
            # self.emps = self.cursor.fetchone()
            if self.cursor.fetchone():
                self.id_exists = True 
                print(self.id_exists)
                             
            else:
                self.id_exists = False
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
        return self.id_exists
    def insert_emp(self, id, name):
        self.sql = "INSERT INTO emp values (%s, '%s')" % (id, name)
        print(self.sql)
        try:
            self.conn = sqlite3.connect("c:\\sqlite\\company.db")
            self.conn.execute(self.sql)
            self.conn.commit()
            print(self.emps)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def update_emp(self, id, name):
        self.sql = "UPDATE emp SET name = '%s' WHERE id = %s" % (name, id)
        print(self.sql)
        try:
            self.conn = sqlite3.connect("c:\\sqlite\\company.db")
            self.conn.execute(self.sql)
            self.conn.commit()
            print(self.emps)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def delete_emp(self, id):
        self.sql = "DELETE FROM emp WHERE id = %s" % id
        print(self.sql)
        try:
            self.conn = sqlite3.connect("c:\\sqlite\\company.db")
            self.conn.execute(self.sql)
            self.conn.commit()
            print(self.emps)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

class AppManager:
    def main(self):
        self.empmgr = EmpManager()
        while True:
            # self.empmgr = EmpManager()
            print("# 사원관리")
            print("#########################")
            print("1. 전체사원검색")
            print("2. 사원검색")
            print("3. 사원추가")
            print("4. 사원수정")
            print("5. 사원삭제")
            print("6. 종료")
            print("#########################")
            sel = input("메뉴를 선택해주세요.(1-6):")
            if sel == '1':
                self.emps = self.empmgr.select_emp()
                for (self.id, self.name) in self.emps:
                    print(self.id, self.name)
                time.sleep(2)
            if sel == '2':
                self.id = input("아이디를 입력해 주세요.: ")
                self.emps = self.empmgr.select_emp_id(self.id)
                print(self.emps)
                time.sleep(2)
            if sel == '3':
                self.id = input("아이디를 입력해 주세요.: ")
                self.name = input("이름을 입력해 주세요: ")
                insert_emp()
                # print(self.sql)
            if sel == '4':
                pass
            if sel == '5':
                pass
            if sel == '6':
                print("감사합니다. 잘가")
                break
            else:
                print("잘못선택했어 토닥토닥")
            
        #CRUD : #https://newstars.tistory.com/436
        # self.empmgr = EmpManager()
        # self.empmgr.select_emp() #table(2) 차원형태가 나옴
        # self.empmgr.select_emp_id(1) #able(2) 차원형태가 나옴
        #self.empmgr.check_id(1) #true or false
        # self.empmgr.insert_emp(10, 'gangga') #None / n개 affected
        # self.empmgr.update_emp(1, 'dfd') #None / n개 affected
        # self.empmgr.delete_emp(1) #None / n affected
        # self.empmgr.check_id(5)

if __name__ == "__main__":
    run = AppManager()
    run.main()
    