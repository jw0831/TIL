#magic method 까지 했었음
#class 와 object 의 차이를 알자!
#self 가 들어 가는건 인스턴스 값

mm = 6
if mm == 0:
    class Person:
        pass

    p1 = Person()
    p2 = Person()
    p3 = p1
############################################################
if mm == 1:
    class Person2:
        count = 0
        def __init__(self):
            self.name = "이순신"
            self.age = 20

        def displayInf(self):
            print(self.name, self.age)

    p4 = Person2()
    
    p4.displayInf()
    p4.name = "whatsup man"
    p4.age = 40
    p4.displayInf()
############################################################
if mm == 2:
    class Person3:
        def __init__(self):
            print("Constructor")

        def __del__(self):
            print("Destructor")

    p5 = Person3()
############################################################
# 오버로딩(Overloading)은 클라스 안에서만(Only Class) 사용한다. 
# 오버라이딩(Overriding) 상속관계 (Class inheritance) 상위에 있는 클라스의 정의되어 있는 메서드를 제정의 하는것
if mm == 3: 
    class Person4:
        def __init__(self, name='', age = 0):
            self.name = NameError
            self.age = age

        def displayInfo(self, name='', age = 0):
            self.name = name
            self.age = age

    p6 = Person4('이순신')
    p7 = Person4("생성자의 오버로딩", 40)

    #Method 의 오버로딩
    
    p6.displayInfo('홍길동')
    p6.displayInfo('오로', 30)
############################################################
if mm == 4:
    class Person5:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age

        def setName(self, name):
            self.__name = name
        def getName(self):
            return self.__name
        
        def setAge(self, age):
            self.__age = age
        def getAge(self):
            return self.__age


    p8 = Person5("이순신", 50)
    print(p8.getName(), p8.getAge())
############################################################
#상속성
if mm == 5:
    class Student:
        def studying(self):
            print("Student Studying")

        def eating(self):
            print("Student Eating")
    class MiddleStudent(Student):
        #상속 : 변수 이름 그대로 사용가능
        def studying(self):
            print("MiddleStudent Studying")
    p9 = Student()
    p9.studying()

    p10 = MiddleStudent()
    p10.studying()
    p10.eating()

if mm == 6: #클래스의 special method / magic method
    class Point:
        def __init__(self,a):
            self.a = a
        
        def __add__(self, other): #+1 이라는 의미
            r = self.a + other.a
            p = Point(r)
            return p

    p10 = Point(1) #{Point : a = 1}
    p11 = Point(2) #{Point : a = 2}
    p12 = p10.__add__(p11)
    print(p12.a)

#python design pattern 공부 검색



# https://legacy.python.org/workshops/1997-10/proceedings/savikko.html
# https://python-patterns.guide/


