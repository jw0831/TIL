from array import *
# arr1 = array('i',[10,20,30,40]) #'i' = type code -> integer
# print(arr1)
# for x in arr1:
#     print(x)

# print(arr1[0])

# arr1.insert(1, 100)
# print(arr1)

# arr1.remove(40)
# print(arr1)
# arr1[0] = 33
# print(arr1)

###############
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# num3 = int(input("num3: "))

# total = 0
# total += num1
# total += num2
# total += num3 
# print(total)
###############
#array 를 사용할 경우

# arr2 = [None] *3 #[None, None, None]

# arr2[0] = int(input("num1 :"))
# arr2[1] = int(input("num2 :"))
# arr2[2] = int(input("num3 :"))

# sum2 = 0
# for i in arr2:
#     sum2 += i
# print(sum2)

# 배열 원소 (3개)의 최대값을 구하시오 . (입력을 3개 받는다.)
# arr2 = [None] *3 #[None, None, None]

# for i in range (0,3):
#     arr2[i] = int(input("num " + str(i+1)+ ":"))

# print(max(arr2))

#teacher
# maxvalue = m[0]
# if m[1] > maxvalue: maxvalue = m[1]
# if m[2] > maxvalue: maxvalue = m[2]

# print(maxvalue)

#함수 maxvalue(........)구현하시오.
#제 사용 하려면 함수가 필요함
#리스트를 array개념으로 사용
# def maxvalue(arr):
#     max2 = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] > max2: max2 = arr[i]
#     return max2

# r = maxvalue([10,2,3,4,30])
# r2 = maxvalue([200,10,23,40,50])
# print(r, r2)


# a, b = map(int, input().split())
# print(a+b)

# a, b = map(int, input().split())
# print(a-b)

#배열을 역으로 정렬하시오
#[10, 2,3,4,5] -> [10,5,4,3,2]
# arr = [10,2,4,5,6]
# arr.sort()
# arr.reverse()
# print(arr)
# Teacher's



# def reverseArr(a):
#     n = len(a)
#     for i in range(n//2):
#         a[i], a[n-i-1] = a[n-i-1], a[i]
#     return a
    
#         # 0 : 3
#         # 1 : 1
#         # 2 : 5


# b = reverseArr([3,1,5]) #return 해준것을 변수로 받아줘야함
# print(b)




#구구단
# n = int(input())
# for i in range (1, 10):
#     print("{} * {} = {}".format(n, i, n*i))

#AI
#Developer, Python, Java, Java Design patter, String Framwork
#Database Oracle, SqlServer, MySql, MariaDb, Mongodb, modeling
#Web Technology(HTML, Javascript, css3, Jquery, Javascript framework)
#cloud platform (Amazon, Azure, Google)..Devops...
#Android, IOS...
#Networking, Shell, Linux admin...


t = [[1,2,3,4],[3,4,5,6],[4,5,6,3],[4,5,3,2]]
print(t[0], t[1], t[2], t[3])
print(t[0][0], t[1][1])
#전부 뽑아내기
for i in t:
    for j in i:
        print(j, end=' ')

