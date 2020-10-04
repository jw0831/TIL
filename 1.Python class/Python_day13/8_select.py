# for i in range(4): #0~3
#     print(i, end=" ")
# print('')

# for i in range(1,4): #1~3
#     print(i, end=" ")
# print('')

# for i in range(1,10,2):
#     print(i, end=" ")
# print('')

# for i in range(10,0,-1):
#     print(i, end=" ")
# print('')

data = [20,1,3,10,12,18,21,100] #len = 8

for i in range(len(data)-1,0,-1):
    # print(i, end=" ")
    max_pos = 0
    for j in range(1, i+1):
        # print(i, '',j,'', end=" ")
        #7 1   7 2   7 3   7 4   7 5   7 6   7 7  
        #6 1   6 2   6 3   6 4   6 5   6 6  
        #5 1   5 2   5 3   5 4   5 5  
        #4 1   4 2   4 3   4 4  
        #3 1   3 2   3 3  
        #2 1   2 2  
        #1 1  
        #[1, 3, 10, 12, 18, 20, 21, 100]
        if data[j] > data[max_pos]:
            max_pos = j
    temp = data[i]
    data[i] = data[max_pos]
    data[max_pos] = temp

print(data)

###############################################################################
# 다른 방법

for i in range(len(data)):
    min_value = i
    for j in range(i+1, len(data)):
        if data[j] < data[min_value]:
            min_value = j
    data[min_value], data[i] = data[i], data[min_value] #python은 temp 사용 안해도 현재 값을 바꿔치기 할수 잇따따 따따따 따따따.

print(data)
