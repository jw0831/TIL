########################################
'''
for 문의 기본 구조
for 변수 in 리스트 (또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
'''
########################################
# s = "Hello"
# for i in s:
#     print(i)
'''
H
e
l
l
o
'''
########################################
# l = [1,2,3,4,5,6,7]
# for i in l:
#     print(i)
########################################
# add = 0
# for add in range(0,10):
#     add = add + 1
#     print (add)
########################################
# l = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in l:
#     print(sum, i)
#     sum = sum + i
########################################
# a = [(1,2),(3,4),(5,6)] #[tuple]
# for(first, last) in a:
#     print(first+last)
########################################
# d = [(1,2),(3,4),(5,6)]
# for item in d:
#     print(item[0], item[1])
########################################
# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print("Student No.%d is Pass" % number)
#     if mark < 60:
#         print("Student No.%d try your best" % number)
########################################
# for i in range(10):
#     print(i+1)
# print("--")
########################################
# for i in range(1,10):
#     print(i, end=" ")
# print("--")
########################################
# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j, end=" ")
#     print("")
########################################
#원하는 단수를 넣으면 구구단을 출력 하시오.
# num1 = int(input("원하는 구구단 단수를 입력하세요:"))
# if 0<num1<10:
#     for j in range(1,10):
#         #print(num1*j, end=" ")
#         print("{} * {} = {}".format(num1, j, num1*j))
# else:
#     print("wrong input")
########################################
#list 내포
########################################
'''
'Python'
['P','y','t','h','o','n']
'''
# letters =[]
# for l in 'Python': #list 안에 for 구문을 넣어주면 굉장히 편하다! 
#     letters.append(l) #list로 만들어주고 싶다
# print(letters)
################다른방법#################
# letters2 = [letter for letter in 'Python']
# print(letters2)
########################################
a = [1,2,3,4,5,6]
b = []
for i in a:
    if(i%2 == 0):
        b.append(i)
print(b)
##############다른방법으로 만들어보기######
c = [num for num in a if num % 2 == 0]
print(c)