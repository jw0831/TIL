pac = 0

if pac == 1:
    class Account:
        def __init__(self, accNo, name, balance):
            self.__accNo = accNo
            self.__name = name
            self.__balance = balance

        def withdraw(self, price):
            self.__balance -= price
        def deposit(self, price):
            self.__balance += price
        def getBalance(self):
            return self.__accNo, self.__name, self.__balance #여러줄 입력 할때 , \ 입력
        # def setBalance():
        #     self.__balance = balance
        #     self.__accNo = accNo
        #     self.__name = name
    
    c = Account(10, '이순신', 2000)
    print(c.getBalance())
    c.withdraw(100)
    print(c.getBalance())
    c.deposit(10000)
    print(c.getBalance())
else:
    pass
#magic method
'''
   " ipython 에서 " 
    num = 10
    num.__add__(20)
    dir(num)
########################
In [7]: num = 20

In [8]: num.__add__(20)
Out[8]: 40

In [9]: num
Out[9]: 20

In [10]: num + 30
Out[10]: 50

In [11]: num
Out[11]: 20

In [12]: int.__str__(num)
Out[12]: '20'

In [13]:                   
'''
'''
page 400 주변 공부
'''

meth = 3

if meth == 1:
    #magic method 사용법
    class Line:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __add__(self, other): # + => __add__
            return Line(self.a + other.a, self.b + other.b) # 아래 코드로 인해 l1 + l2 가 되는 경우임.

    l1 = Line(1, 2)
    l2 = Line(3, 4)
    # print(l1 + l2) 이런식으로 이해하면됨
    # l1.__add__(l2)
    l3 = l1 + l2
    print(l3.a, l3.b)

    l3 = l1.__add__(l2) #(괄호 안에 들어온게 other 임)
    print(l3.a, l3.b)

elif meth == 2:
 #다른 방법
    class Point:
        def __init__(self, a): #내장 인스턴스 변수를 하나만 만들어줌
            self.a = a
        def add(self, p2): # p1.add(p2)  p2 는 임의로  
            # r = self.a + p2.a
            # p3 = Point(r)
            # return p3
            # 한줄로 적게 되면
            return Point(self.a + p2.a)
        
    

    p1 = Point(1)
    p2 = Point(2) 
    p3 = p1.add(p2) 
    
    print(p3.a)
    
elif meth == 3:
 #다른 방법
    class Point:
        def __init__(self, a): #내장 인스턴스 변수를 하나만 만들어줌
            self.a = a #퍼블릭 상태임 (프로텍트, 프라이빗 아님)
        def __add__(self, write_any): # p1.add(p2)  p2 는 임의로  교재 에서 는 other 로 씌여있음 아무거나 들어가면됨
            # 한줄로 적게 되면
            return Point(self.a + write_any.a)
            # r = self.a + p2.a
            # p3 = Point(r)
            # return p3     

    #인스턴스 변수를 사용한다는 것은 공유하지 않고 자체적으로 쓰겠다는 것임.
    p1 = Point(1)
    p2 = Point(4) 
    # p3 = p1.add(p2) 
    p3 = p1 + p2 #위에 meth 2 와 비교했을때 훨씬 간결하게 작성할 수 있어서 이런 의미로 만들어서 사용하는 것이다!!
    print(p3.a)

elif meth == 4:
    class Point:
        def __init__(self, a):
            self.a = a
        def __add__(self, p2):
            self.a #1
            p2.a #2

    p1 = Point(1) #이친구 관점으로 기준으로 먼저 보고 위에 작성하면된다.
    p1.a #1
    p2 = Point(2)
    p2.a #2

'''
http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-oop-part-6-%EB%A7%A4%EC%A7%81-%EB%A9%94%EC%86%8C%EB%93%9C-magic-method/
https://wikidocs.net/83755
https://dojang.io/mod/page/view.php?id=2373
'''