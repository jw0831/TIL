#python documentation 구글에 검색
# 빠른검색에 print() 검색 하면 기능이 설명되어 있는것을 확인 할 수 있음.
#https://docs.python.org/ko/3/library/functions.html#print

#파일 읽고 쓰기.

'''
with 을 사용하면 더 가독성 있게 쓸수 있도록 도와준다.. 기능적인 차이는 별로 없다..

f = open("foo.txt", 'w')
f.write("LLife is too short, ou need pyton")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, ou need pyton")
위에 것과 달리 f.close()가 필요 없다.. 자동으로 close. 위에것을 추천.. 가독성을 위해

'''
##########################################################################################
##########################################################################################
'''
#5장  Object Oriented Language (OOP) 객체지향 언어

OOP 의 목적은 재사용을 좋게 하는 것이다!!!

함수만 사용하다 보면 여러함수가 서로 연관되어서 나중에 변수를 수정 하게 되면 그것에 
파생된 변수가 많이 변하게 된다.

클래스라는 틀을 만들어서 해당되는 변수를 묶어서 이런 함수들의 수정과 같은 어려움을 해소

연관되는 데이터들만 모아서 하게되면 유지 보수에 용이함...!

객체지향 프로그래밍 (OOP의 특성)
-캡슐화
-상속성
-다형성

--------.py---------
|| 변수(variables)   ||
|| 함수(funcitons)   ||
|| 클래스(class)     ||
--------------------
pg. 377 - 383
class(설계도) 와 object(객체) 의 차이 잘 알아야함
'''
'''
###### class 선언 부분 ######
class Student:
    name = "홍길동"
    age = 20

    def gotoSchool(self):
        print(self.name, self.age)
#memory 에 올려주고 사용~
###### 메인 코드 부분 ######
s = Student()
s.gotoSchool()
########################################################################
'''
########################################################################
st = 3
# st = 2

if st == 1:
    class stSystem:
        no = 0
        name = ""
        grade = 0

        def study(self, no, name, grade):
            self.no = no
            self.name = name
            self.grade = grade

    s1 = stSystem()
    s1.study(10, '홍길동', 3)
    s2 = stSystem()
    s2.study(20, '강감찬', 2)
########################################################################
elif st == 2:
    class stSystem:
        no = 0
        name = ""
        grade = 0

        def __init__(self):
            self.no = 10
            self.name = "강감찬"
            self.grade = 3

        def study(self):
            print(self.no, self.name, self.grade)

    s1 = stSystem()
    s1.study() #생성자로 인해 값이 초기화 된 상태

    s2 = stSystem()
    s2.no = 2
    s2.name = "what"

    s2.grade = 100
    s2.study()

else:
    pass
########################################################################
run = 3
# run = 2

if run == 1:
    ###### class 선언 부분 ###### 객체지향적은 속성과 동작을 분류해주면 좋다.
    class Car:
        #속성
        color = ""
        speed = 0
        #동작
        def upSpeed(self, value):
            self.speed += value

        def downSpeed(self, value):
            self.speed -= value

    ###### 메인 코드 부분 ######

    myCar1 = Car()
    myCar1.color = "red"
    myCar1.speed = 60

    myCar1.upSpeed(30)
    print("Car1 is %s and it's current speed is %d" % (myCar1.color, myCar1.speed))

elif run == 2:
    ########################################################################
    class Car :
        color = ""
        speed = 0

        def __init__(self,value1,value2):
            self.color=value1
            self.speed=value2

        def upSpeed(self, value):
            self.speed += value

        def downSpeed(self, value):
            self.speed -= value

    myCar1 = Car("Red", 30)
    myCar2 = Car("Blue", 60)

    print("Car1 is %s and it's current speed is %d" % (myCar1.color, myCar1.speed))
    print("Car1 is %s and it's current speed is %d" % (myCar2.color, myCar2.speed))

elif run == 3:
    #Employee
    #속성: name, age
    #동작: working
    class Employee:
        def __init__(self, name='empty', age=0):
            self.name = name
            self.age = age
            
        def working(self):
            print(self.name, self.age)

    e0 = Employee()
    e0.working()

    e1 = Employee('홍길동', 30)
    e1.working()

    e2 = Employee('고길동', 20)
    e2.working()
else:
    pass