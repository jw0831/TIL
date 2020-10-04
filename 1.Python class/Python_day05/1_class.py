#클래스를 이용한 계산기

#디자인 =
#사람
#속성 : 이름, 나이
#동작 : 걷는다.

class person:
    #필드
    name = ""
    age = 0

    #메서드
    def walking(self):
        print(self.name, self.age)


p = person() #인스턴스 생성

#인스턴스.필드
p.name = "홍길동"
p.age = 30
#인스턴스.메서드
p.walking()

class person2:
    name = "dddd" #예는 다 공유가 되는거다..
    age = 0

    #생성자
    def __init__(self, name, age):
        self.name = name #self 가 붙으면 인스턴스가 있을때만 나온다.
        self.age = age
    def walking(self):
        print(self.name, self.age)

g = person2("",9)
g.walking()
p2 = person2("이순신", 100)
p2.walking()

#page 391 읽기 꼭!!
