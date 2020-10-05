# print(abs(-1.2))

sum = 0
for i in range(1,11,1):
    sum += i
    print(i, end=" ")
    print(sum)
# extend = merging
# append = 항목이 들어간다

# l3 = [1,2,3,4]
# l3.append((5,))
# print(l3)

# l3.append({'name':'john'})
# print(l3)

# l4 = [[1,2,3,],[4,5,[1,2,3]]]
# print(l4[1][2][1])

# # 캡슐화, 상속성, 다형성 에 대해서 알아야한다.

# %% 
# https://wikidocs.net/13

# collection 
# tuple, list, dictionary

# searching 정렬이 되어있는상태
# 스택, 큐
list = [1, 2, 3] 
a = list.append([4])
print(list)

n = 5
factorial = 1
for i in range(1, int(n)+1):
	factorial = factorial * i
print(factorial)