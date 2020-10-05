###################################################
'''
def sum(a, b):
    return a + b

x = int(input("num1: "))
y = int(input("num2: "))

z = sum(x, y)
print("Sum =", z)
'''
###################################################
'''# 사용하다보니 가변적인 파라미터가 발생해서 함수에 *입력하면 여러개 포함할수있도록 해준다
###################################################
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum_many(1,2,3,4,5), type(sum_many()))
print(sum_many(10,20,30,40,50))'''
###################################################
#tuple 형태로 나오게 된다..!
# def printNames(*names):
#     print(type(names))
#     for name in names:
#         print(name)
# #<class 'tuple'>

# printNames('이순신', '홍길동', '이순신')
# printNames('강감찬', '권율')
####################################################
#함수의 결과 값은 언제나 하나이다
####################################################
'''
def calc(a, b):
    return a+b, a-b

result = calc(4,2)
print(result, type(result))
print(result[0], type(result[0])) #indexing 으로 뽑아냄             ***
'''
####################################################
#optional parameter / "man = True" / def say_myself(name, old, man = True)
####################################################
'''
def printMe(name, age = 20, man=True): #man = True 같은 optional parameter들은 뒤에다가 작성하기!
    print(name, age, man)
    if man:
        print("man")
    else:
        print("woman")

printMe("홍길동") #값을 안들어갔을때에는 디폴트로 20이 됨
printMe("이순신", 40)
printMe("울랄라", age = 6) #그냥 이런 방법도 있다.
printMe(age = 50, name = '이런방법도..', man = False)
'''
########### <dicitonary 형태로 받는경우> #############
def printPersons(**info): #   ** 넣으면 dictionary
    print(type(info))

printPersons(name='홍길동',age = 20, hobby = '농구')
