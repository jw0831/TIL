ex = 0

if ex == 1:
    class Database:
        def open(self):
            print("Database open")
        
    class Oracle(Database):
        def open(self):
            print("Oracle open")

    class MySql(Database):
        def open(self):
            print("MySql open")

    class MongoDb(Database):
        print("MongoDB openAB")

    o = Oracle()
    o.open()

    o2 = MySql()
    o2.open()
    #다형성 예제

    o3 = MongoDb()
    o3.open()

if ex == 2:
    class Student:
        def __init__(self, name=''):
            self.name = name
            print("Student Constructor", self.name)

    class MiddleStudent(Student):
        def __init__(self):
            super().__init__('이순신') #호출!
            
            print("MiddleStudent Constructor")

    s = MiddleStudent()

if ex == 3:
    class Car:
        value = '슈퍼 값'
        def carMethod(self):
            print('슈퍼 클래스 메서드 실행~~')

    class Sedan(Car):
        value = '서브 값'
        def carMethod(self):
            super().carMethod()
            print()


######################################################################################################
#accessor (접근자): public, private(__), protected(_)

em = 3

if em == 1:
    class Employee:
        __test = 10 #private 라 접근이 안됨 안에서만 쓰도록 막아 주는것
        def __test2(self): #private function
            pass
    
        def __init__(self, name, salary):
            self._name = name           #protected(_) variable
            self._salary = salary       #protected(_) variable

    e = Employee("이순신", 200)
    print(e._name, e._salary)
    #print(e.__name, e.__salary) #private

elif em == 2:
    class Employee: #캡슐화 (data hide)
        def __init__(self, name, age):
            self.__name = name #얘는 항상 숨겨주는게 객체지향적 코딩 방법에 적합하다. 정보들은 숨겨주는것 이 옳다.
            self.__age = age

        def getName(self): #접근할때 이것과
            return self.__name

        def getAge(self): #이것만 사용 해서 불러오는 것을 인캡슐레이션이라고한다. 
            return self.__age

        def setName(self, name):
            self.__name = name

        def setAge(self, age):
            self.__age = age

    e = Employee("이순신", 30)
    #e.name 으로 접근이 안된다 메서드로 해야된다 protect 에서는
    print(e.getName(), e.getAge())

elif em == 3:
    class Student1:
        def __init__(self, name=''):
            self.__name = name
        def getName(self):
            return self.__name
        def setName(self, name):
            self.__name = name

    s = Student1("홍길동")
    print(s.getName())
    s.setName("이순신")
    print(s.getName())