# a = 100
# print(a > 100)
# if(a>100): #False 이기 때문에 True를 채워야 값이 나오겠지~
#     print("a > 100")
'''
a1 = int(input("숫자를 입력해주세요. "))
if(a1 > 10):
    print("a1 > 10 크다.")
    print("end")
else:
    print("a1 < 10 작다.")
    print("end")
'''

#두수를 입력하고 원하는 연산자를 입력한 경우, 연산 처리하는 부분을 구현하시오.

num1 = int(input("첫번째 숫자를 입력해주세요. : "))
op = str(input("원하는 연산자를 입력하시오 : "))
num2 = int(input("두번째 숫자를 입력해주세요. : "))
ans=0
#답 : 3 + 1 = 4 입니다.

if op == "+" :
    ans = num1+num2
    print("{} + {} = {}입니다." .format(num1, num2, ans))
if op == "-" :
    ans = num1-num2
    print("{} - {} = {}입니다." .format(num1, num2, ans))
else:
    print("input error")