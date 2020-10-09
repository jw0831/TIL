inherit = 4

if inherit == 1:
    class Animal:
        def breathing(self):
            print("Animal breathing")

    class Bird(Animal): #bird가 animal 에게 상속 받음. 로직을 계속 사용할 수 있게 됨
        def flying(self):
            print("Bird Flying")
        
        # def breathing(self):
        #     print("Bird breathing") #위에 에니멀에서 쓰고 있지만 동일한것을 다른 내용으로 할때 오버라이딩을 한다. ***

    class Dog(Animal):
        def barking(self):
            print("Dog barking")

    o = Bird() #class bird 를 사용했지만 상속효과로 인해서 Animal 도 작동됨.
    o.breathing()
    o.flying()


    #o.barking()     #은 서로 상속이 안되서 안된다.!!
    d = Dog()
    d.barking()
    d.breathing()
##################################################################################################
    
elif inherit == 2:
    class Car:
        def speedUp(self):
            print("자동차가 달린다")

    class Truck(Car):
        def speedUp(self): # Overriding (class 상속간의 관계)
            print("트럭이 달린다")
        
    c = Truck()
    c.speedUp()
##################################################################################################

elif inherit == 3:
    class Car:
        def __init__(self, speed = 10, gearType = 1): #Overloading 옵셔널 하게 작성    __init__ 생성자로 해야 가능함
            self.speed = speed
            self.gearType = gearType
            print("자동차가 달린다")
            print(self.speed, self.gearType)

    class Truck(Car):
        def speedUp(self): # Overriding (class 상속간의 관계)
            print("트럭이 달린다")
        
    c = Truck()
    c.speedUp() #over riding
    c2 = Car()
    
    c3 = Car(30, 5) #over loading

    
##################################################################################################    
elif inherit == 4:
    class Student:
        #constructor overloading
        def __init__(self, name='', age=0):
            self.name = name
            self.age = age
            print(self.name, self.age)

        def studying(self, name='', age=0): #생성자에 대한 오버로딩
            self.name = name
            self.age = age
        
            print(self.name, self.age)
            # return self.name, self age 

    class MiddleStudent(Student):
        #def __init__():
        
        def studying(self):
            print("중학생")

    s = Student('wow')
    s1 = Student('lee')
    s3 = Student('kim', 29)

    s.studying()
    s.studying('Overloading on consructor', 10)

    s.name ='jin'
    s.age = 19
    print(s.name, s.age)

    s2 = MiddleStudent("와따", 9)
    s2.studying()
'''
class에 print 말고 return 도 사용할 수 있다.
'''

##################################################################################################    
#다형성: 상속관계에서 서로 다른 속성을 보임.

##############################################################################################################

##############################################################################################################
'''
#class vs object(instance)
class --> instance 화 시키는 과정에 vairable..(init) 생성자 (constructor -> __init__)
variable..(destroy) -> destructor -> __del__
'''
pt = 0
if pt == 1:
    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
        
        def __del__(self):
            class_name = self.__class__.__name__
            print(class_name, "destroyed") #Point destroyed 가 나오겠지..

    p1 = Point()
    p2 = p1 #객체 왔다 갔다.
    p3 = p2
    print(id(p1), id(p2), id(p3))#객체 생성된 고유 넘버 확인 가능 1568446138248 1568446138248 1568446138248 모든 ID 가 같게 나옴 : 객체가 1개라는 뜻
    del p1
    del p2
    del p3

elif pt == 2:
    pass