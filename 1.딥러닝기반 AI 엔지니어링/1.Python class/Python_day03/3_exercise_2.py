################################################
#Overloading 이라고 한다..
#파이썬은 보통 함수를 이런식으로 사용한다.
################################################
'''
def add(a, b=0, c=0):
    return a+b+c

print(add(1))
print(add(1,2))
print(add(1,2,3))
'''
################################################
#무한히 만들어 주고 싶은 경우 곱하기 를 쓴다. *args
################################################
#확장성을 고려할 경우 이렇게 사용하는게 좋다.
#프로그래밍은 상상력을 발휘해서 하면 힘들다.. 요구사항대로 만들어 주면 된다.
'''
def add10(*a): #여러 값이 들어올수 있다.
    sum = 0
    for i in a:
        sum += i
    return sum

print(add10(1))
print(add10(1,2))
print(add10(1,2,3), type(add10()))
'''
# 비록 많이 사용되지는 않지만, **의 장점 key & value가 쌍으로 있는 상태에서 사용하면 좋음
# 'word1' = '홍, 'word2' = '길', 'word3; = 동

def concate(**words):
    result = ''
    print(words.values())
    for w in words.values():
        result += w
    return result

ret = (concate(word1 = '홍', word2 = '길', word3 = '동'))
print(ret)
