#refer to page 389
#클래스 변수와 인스턴스 변수의 차이점을 잘 알자!!

'''
class myclass:
    i = 0 #class variable
    def __init__(self):
        self.i = 2000 #instance variable
        myclass.i = 1000 #class variable



s= myclass()
print(s.i)
print(myclass.i)
'''
c = 2

if c == 1:
    class Account:
        balance = 0
        def __init__(self, name):
            self.name = name #클래스 안에 self 가 붙으면 인스턴스구나 라고 알면 되겠다.. 그러므로 공유가 안된다..
            Account.balance += 1 #생성 할때마다 + 1 시키겠다. / 공유가 됨

    Jade = Account('Jade')

    print(Account.balance)

    John = Account('John')

    print(Account.balance, ": class가 공유가 되어서 2로 올라간 것을 볼 수 있다.")

elif c == 2:
    class Employee:
        empCount = 0 # Class variable
        def __init__(self, name, salary): #생성자 (Constructor)
            self.name = name
            self.salary = salary
            Employee.empCount += 1
#현재까지 생성자였다.
        ####소멸자 또한 존재한다. 삭제 할일이 있으면 사용####
        def __del__(self): # destructor 소멸자
            class_name = self.__class__.__name__
            print(class_name, "destroyed")
        #################################################
        def displaycount(self):
            print(Employee.empCount)

        def displayEmployee(self):
            print(self.name, self.salary)

    emp1 = Employee("kim", 5000)
    emp1.displaycount()
    emp1.displayEmployee()

    emp2 = Employee("Lee", 4000)
    emp2.displaycount()
    emp2.displayEmployee()




