# a = 1
# b = 2
# c = a
# a1 = a
# a = 3
# a = 'test'
# print(a1)
# print(a)

#문자열 포매팅
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
print("%d %d" % (number, number))
c1 = 2
c2 = 3
d = c1 + c2
print("결과는 %d" % d)
print("%d 더하기 %d = %d" % (c1, c2 , d)) #두개이상은 괄호 필수
#사용 예:  1000.200 일때 d 만 딱 넣어주면 1000 만 나오고 포매팅 하고싶을때 사용
# % 는 포매팅을 하겠다!

# print("%d/%d=%5.2f" % (100, 200, 0.5))

# print("%d" % 123)
# print("%5d" % 123)
# print("%05d" % 123)

# print("%f" % 123.45)
# print("%7.1f" % 123.45)
# print("%7.3f" % 123.45)

# print("%s" % "Python")
# print("%10s" % "Python")

#format 기능
print("결과는 {}, {} {}".format(c1, c2, d))
print("결과는 {1:}, {0:>3d} {2:}".format(c1, c2, d)) #순서 및 위치 바꾸는법 ex) 0.054+e10 같은 것 포멧하기 편안함

print("결과는 {0:>5d}".format(500)) #화살표 방향으로 밀림

#이스케이프 문자 [pg.66]
print("\n줄바꿈\n연습")
'''
ctrl + a
ctrl + /'''
#--------------------------------------------------------------------------------------------------------
'''a = input("첫번째 숫자를 입력해주세요: ")
#print(a)
b = input("두번째 숫자를 입력해주세요: ")
print(type(a), type(b))
c = a + b
print(c, type(c))'''
a1 = int(input("첫번째 숫자를 입력해주세요: "))
b1 = int(input("두번째 숫자를 입력해주세요: "))
c1 = a1 + b1
print(c1, type(c1))
# "a와 b의 합은 + c 입니다" 불편함
print("{}와 {}의 합은 {}입니다." .format(a1, b1, c1))

