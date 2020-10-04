#다음의 데이터를 bubble sort를 하고 binary search를 하여 결과값이 있는지 검색하시오.


key = 12
'''
for sort in range(len(data)-1,0,-1): #7 6 5 4 3 2 1
    # print(sort)
    for bubble in range(sort): #0~6 = 7개
        # print(bubble)
        if data[bubble]>data[bubble+1]: #6+1 해주니까 7까지 비교를 해줌
            temp = data[bubble+1]
            data[bubble+1] = data[bubble]
            data[bubble] = temp
            #data[bubble], data[bubble+1] = data[bubble+1], data[bubble]
print(data) #data is sorted
'''
# #mine
# def loopBubble(len(data)):
#     if len(data) >= len(data)-1
#         sortBubble(data)
#         return len(data)-1

# def sortBubble(data[bubble],data[bubble+1]):
#     if data[bubble] == data[bubble+1]:
#         return True
#     elif data [bubble] > data[bubble+1]:
#         return sortBubble(data[bubble+1],data[bubble])
#     else:
#         print("error")

# data = [20,1,3,10,12,18,21,100] #len = 8
# a = loopBubble(data)
# print(a)

#teacher
#Bubble Sort -> Recursion 재귀함수
data = [20,1,3,10,12,18,21,100]

# #1 pass
# 5 1 4 2 8 -> 1 5 4 2 8
# 1 5 4 2 8 -> 1 4 5 2 8
# 1 4 5 2 8 -> 1 4 2 5 8
# 1 4 2 5 8 -> 1 4 2 5 8
# #2 pass
# 1 4 2 5 8 -> 1 4 2 5 8
# 1 4 2 5 8 -> 1 2 4 5 8
# 1 2 4 5 8 -> 1 2 4 5 8

def bubblesort2(data, n):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
        if n>1:
            bubblesort2(data, n-1)

n = len(data)
bubblesort2(data, n)
print(data)
