import sqlite3

class EmpManager:
    def select_emp(self):
        self.sql = "SELECT * FROM emp"
        try:
            self.conn = sqlite3.connect("c:\\sqlite\\company.db")
            self.cursor = self.conn.execute(self.sql)
            self.emps = self.cursor.fetchall()
            print(self.emps)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
        return self.emps

    def select_emp_id(self, id):
        self.sql = "SELECT * FROM emp where id = %s" % id
        print(self.sql)
        try:
            self.conn = sqlite3.connect("c:\\sqlite\\company.db")
            self.cursor = self.conn.execute(self.sql)
            self.emps = self.cursor.fetchall()
            print(self.emps)
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
        return self.cursor
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
        #CRUD : 
        self.empmgr = EmpManager()
        # self.empmgr.select_emp() #table(2) 차원형태가 나옴
        # self.empmgr.select_emp_id(1) #able(2) 차원형태가 나옴
        #self.empmgr.check_id(1) #true or false
        # self.empmgr.insert_emp(10, 'gangga') #None / n개 affected
        # self.empmgr.update_emp(1, 'dfd') #None / n개 affected
        # self.empmgr.delete_emp(1) #None / n affected
        self.empmgr.check_id(5)

if __name__ == "__main__":
    run = AppManager()
    run.main()
    