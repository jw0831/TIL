'''
#eval 문자열을 받아서 수칙계산가능 , ASCII 에 숫자 범위 넘어가는 애들 체크해서 오류 막기.

a = input("a : ")
b = input("b : ")
op = input("op : ")

print(type(a), type(op), type(b))
c = a + op + b
print(c)
d = eval(c)
print(d)
'''
'''
#filter
def a(b):
    return b>10

f = filter(a, [10,11,-1,100,200])
print(list(f))
'''
'''
#hex
print(hex(0))
'''
############################################################################
# def test(a):
#     return a > 10

# test2 = test
# print(test2(10))

# for i in [10, 20, 30, 40,-1]
#     print(i)

# list1 = [10, 20, 30, 40,-1]
# test = []
# def filter2(func, list1):
#     list2 = []
#     for i in list1:
#         if func(i):
#             list2.append(i)
#     return list2 #return   list

# filter2(test, [20,100,30,-1])

# filter2(lambda a:a > 10, [20,100,30,-1])
############################################################################
#map
def test2(x):
    return x * 2

def map2(func, list1):
    list2 = []
    for i in list1:
        list2.append(func(i))
    return list2

print(map2(test2, [1,2,3,4]))
