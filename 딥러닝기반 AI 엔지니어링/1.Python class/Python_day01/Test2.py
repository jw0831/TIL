#type 으로 함수의 서식을 확인할 수 있다.
a = 5 #Integer
print(a)
b = '5' #String
print(b)
print(type(a)) #Define class 나중에 충돌 일어날경우 확인 하는데 좋음
print(type(b))
c = 100.5 #Float
print(type(c))

d = 7/4
print(d, type(d))
d1 = 7//4
print(d1, type(d1))

e = 3
f = 2
g = e ** f
print(g, type(g))

h = 'hello'
h1 = "hello"
print(h, h1, type(h), type(h1))
h2 = "안녕"
print(h + h1 + h2)

'''주석
여러줄 적용하는법
'
'
'
여기까지'''

food = 'Python\'s favorite food is perl' #\' 를 입력하면 어퍼스트러피가 된다
say = "\"Python is very easy.\" he says."
print(food)
print(say)

multiline = "life is too short\nYou need python"
print(multiline)

a3 = 100
a4 = 200
a5 = a4 + a3
a6 = 'test' *2
print(a6)

#******************************************************************
#인덱싱 indexing
a7 = 'Hello, Python 3.7'
print(a7)
print(a7[0], a7[4], a7[-1])

#******************************************************************
#슬라이싱 (Slicing = 자르다)
i = "Life is too short, You need Python"
'''
i[0] #indexing 은 좌측 첫부분이 0으로 시작
i[0:4]#slicing 은 좌측 첫부분이 1로 시작 / 왼쪽에 0이 있다고 생각하면됨
'''
print(i[0:4])
print(i[1:4])#deep learning 할때 슬라이싱 많이 사용하게됨
print(i[3:4])
print(i[4:])
print(i[:5])
print(i[:])
#빵처럼 가로로자르고 세로로 자르고 / 파이선의 강점!
#******************************************************************

