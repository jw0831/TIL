#문자열 자료형
#문자열 개수 세기 (count)
# a = "hobby"
# a.count('b')

#리스트 자료형
list = ['test', 1, 2.50, 'test2']
print(list)
#indexing
print(list[0], list[2])
#slicing
#list[0:1]
print(list[0:1])
print(list[2:])
print(type(list))
print(list * 2)
#리스트 나 인덱싱의 쓰임은 같아서 둘중 하나를 알고 있으면 좋음
print(list[:])
str2 = "Life"
#str2[0] = "T" 안됨
print(str2[0])
#str2[0] = 'S' 안됨 //가져오는것은 되는데 인풋은 안됨

print(list[0])
list[0] = 'S'
print(list[0]) #리스트는 바뀐다!! 내용수정 마음대로 가능
#그래서 리스트를 가장 많이 쓴다. 데이터를 여러 타입을 집어넣고 싶을때.. 머신러닝이나 딥러닝을 할경우
list[0] = [1, 2, 3]
print(list)
#파이썬은 배열을 지원 못하기때문에 리스트를 많이 사용 합니다. ex) e = [1, 2, ['life', 'is']]
print(list[0][0]) #배열처럼 사용가능

