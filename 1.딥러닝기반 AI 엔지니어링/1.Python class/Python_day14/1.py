'''
def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

print(factorial(3))

# factorial(3)
# print(3*factorial(2))
# print(3*(2*factorial(1)))
'''
#생성자 함수 (generator func with yield)
#호출 될때마다 값이 하나씩 나오게 
# def genFunc(num):
#     for i in range (0,num):
#         yield i
#         print('processing generator')
# for data in genFunc(5):
#     print(data)
'''
def generator_test():
    yield 1
    yield '2'
    yield 'test'

generator_test()

for i in generator_test():
    print(i, end=" ")
################
print('')
d = generator_test()
#__next__ 메서드 사용해도 된다.
print(d.__next__(), end=" ")
print(d.__next__(), end=" ")
print(d.__next__(), end=" ")

#deep learning 할때 호출하면 나오게끔 사용할 경우가 있다.
#iterator라고 한다.
'''

def num_generator(n): #iterator ...=> c++ design pattern...java..
    num =1 
    while True: 
        yield num
        if num == n:
            return
        else:
            num+=1

d=num_generator(10000)
print(d.__next__())
print(d.__next__())
print(d.__next__())

for i in num_generator(100):
    print(i)
