##########10 ~ 99 사이의 난수 n개 생성하기
# import random

# n = int(input("난수의 개수: "))
# for _ in range(n): #특별하게 뭐 없을경우 _ 로 대체 가능 
#     r = random.randint(10,99)
#     print(r, end=" ")
#################### continue ##################################
# for i in range(1,15):
#     if i == 7:
#         continue # skip 이라 생각
#     print(i)
##################
# for i in range (1,10):
#     for j in range (1, 10):
#         print(i*j, end=" ")
#     print('')

#구구단 복습!

# 출력 입력한 n값에 대한 삼각형 피라미드 만들기.
# n = int(input("피라밋 층수 : "))
# for i in range (n+1):
#     print("*" * i)

# 오른쪽으로 정렬 ###########################
# n = int(input("피라밋 층수 : "))



# #선생님 답 
# n1 = int(input("개수를 입력해주세요. : "))
# for i in range(n):
#     for _ in range(n-i-1): # n 이 5일 경우  5-0-1, 5-1-1, 5-2-1...
#         print(" ", end='')
#     for _ in range(i+1):
#         print("*", end='') # n 이 5일 경우 0+1, 1+1, 2+1... 
#     print()

# 세개의 정수를 받아서 중앙값을 구하시오

# a = 10
# b = 5
# c = 7 # a < mid=c < 10

# a = int(input("input a: "))
# b = int(input("input b: "))
# c = int(input("input c: "))

# if a > b and a > c:
#     max1 = a
#     if b > c:
#         mid1 = b
#         min1 = c
#     else:
#         mid1 = c
#         min1 = b
# if b > a and b > c:
#     max1 = b
#     if a > c:
#         mid1 = a
#         min1 = c
#     else:
#         mid1 = c
#         min1 = a
# if c > b and c > b:
#     max1 = c
#     if b > a:
#         mid1 = b
#         min1 = a
#     else:
#         mid1 = a
#         min1 = b


# print("{} < {} < {}".format(min1, mid1, max1))

# jh.H
# temp = []
# temp.append(a)
# temp.append(b)
# temp.append(c)

# temp.sort()
# print (temp)
# print("{} < {} < {}".format(temp[0], temp[1], temp[2]))

#teacher's ans

def testmed(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b 

a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))
print(testmed(a,b,c))