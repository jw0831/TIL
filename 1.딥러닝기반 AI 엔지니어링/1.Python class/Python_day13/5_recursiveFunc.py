#부서에서 트리 같은 구조 여러번 많이 만들어야 할때 많이 사용 (회사에서)
'''
data = [1,2,3,7,8,10]
key = 7
low = 0
high = len(data) - 1

def binarySearch2(data, low, high, key):
    if high >= low:
        mid = low + (high- low) //2 #아래 조건부에서 함수가 재귀 되면서 여기의 High 및 Low 값이 변화된다.
        if data[mid] == key:
            return mid
        elif data[mid] > key:
            return binarySearch2(data, low, mid-1, key) #high = mid-1 / 재귀 함수 사용
        else:
            return binarySearch2(data, mid+1, high, key) #low = mid+1 / 재귀 함수 사용
    else:
        return

r =  binarySearch2(data, low, high, key)
print(r)
'''


# # recursive 
# def hello():
#     global counter
#     print("hello")
#     return hello()

# hello()

'''
data = [1,2,3,4]
sum2 = 0
for i in data:
    sum2 += i
print(sum2) #10

def sum3(data):
    if len(data) == 1:
        return data[0]
    else:
        return data[0] + sum3(data[1:]) # 1 +

print(sum3(data)) #10
'''

#factorial
#n!
#n(n-1)(n-2)
# n = 5
# factorial = 1
# if int(n) >= 1:
#     for i in range(1, int(n)+1):
#         factorial = factorial * i

# #5 4 3 2 1 = 120 
# print(factorial)

#recursive factorail 재귀함수: recurrsion
n =5
def myFactorial(n):
    if n == 1:
        return n
    elif n < 1:
        return "Nothing"
    else:
        return n * myFactorial(n-1)

print(myFactorial(n))

