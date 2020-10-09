'''
list1 = [1,2,3,4]
def changeList1(list2):
    print(list2)
    list2[0] = 100
    print(list2)
    if (len(list2) > 0):
        return
    else:
        print("test")

list1 = [1,2,3,4]
changeList1(list1)
print(list1)
'''
#세 정수의 최대값을 구하기
'''
#my ans:
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if (a>b and a>c):
    print("the largest input is a: %s"% a)
elif (b>a and b>c):
    print("the largest input is b: %s"% b)
elif (c>a and c>b):
    print("the largest input is c: %s"% c)
else:
    print("error")
'''
'''
# Teacher's ans:
a = input("a : ")
b = input("b : ")
c = input("c : ")
maxvalue = a
if b > maxvalue: maxvalue = b
if c > maxvalue: maxvalue = c
print(maxvalue)
'''
'''
#홍주혁님
a = input("a : ")
b = input("b : ")
c = input("c : ")
temp = []
temp.append(int(a))
print(temp)
temp.append(int(b))
print(temp)
temp.append(int(c))
print(temp)
print(max(temp))
'''
'''
print(int('17'))
print(int('13', 10))
print(int('0x4f', 16))
'''
# ############입력받은 정수의 부호(양수, 음수, 0)을 출력하기
# a = int(input('정수 입력: '))
# if a == 0:
#     print('0')
# elif a > 0:
#     print('+')
# elif a < 0:
#     print('-')

###################1 부터 n까지 정수의 합을 구하시오
#while, for

# n = int(input("합을 구할 정수: "))
# total = 0
# count = 1
# while count <= n:
#     total = total + count
#     count += 1
# print("1 부터 %d 까지 정수의 합 = %d 입니다" % (n, total))        

# or 

# for i in range (1,int(n+1)):
#     # print(i)
#     total = total + i
# print(total)

################# a 부터 b 까지 정수의 합을 구하시오:

# a = int(input("input a: "))
# b = int(input("input b: "))
# temp = [a, b]
# max1 = int(max(temp))
# print(max1, type(max1))
# min1 = int(min(temp))
# print(min1, type(min1))
# sum = 0
# if max1 - min1 == 1:
#     print(max1+1)
# else:
#     for i in range (min1, max1+1):
#         # print(i)
#         sum += i
#         # i += i     
#     print(sum)

#teacher's logic
# if (a>b):
#     a, b = b, a

# test = [3,3,4,2,1]
# test.sort()
# print(test) #위에거 이걸로 해도 되겠다.

# # teacher's logic
# a = int(input("input a: "))
# b = int(input("input b: "))

# sum = 0
# if (a>b):
#     a, b = b, a
# for i in range (a,b+1):
#     if i < b:
#         s1 = "{} + ".format(i)
#         print(s1, end='')
#     else:
#         s2 = "{} = ".format(i)
#         print(s2, end='')
#     sum += i
# print(sum)

