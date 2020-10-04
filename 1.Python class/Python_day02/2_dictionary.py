##############################################################################
#dictionary (연관값/사전객체) 데이터를 정리해서 만들고 싶다. 키가 중복되지 않게.. mutable 바꿀수 있음
# ##############################################################################
# a = {1: 'a'}
# a[2] = 'b'
# print(a)

# str = []
# str.append('삽입')

# dict1= {'name':str, 'age': 40}
# print(dict1)
# #dict1['name']
# print(dict1['name'])
# print("name : %s, age : %d" % (dict1['name'], dict1['age']))
# dict1['name'] = '변환(mutable)'
# dict1['age'] = 29
# print("name : %s, age : %d" % (dict1['name'], dict1['age']))
# del dict1['name']
# print(dict1)
# dict1['name'] = 'tom'
# print(dict1)
# #dictionary 형태로 사용할경우 리스트에 정리해서 불러옴
# print(dict1.keys()) #딕셔너리의 키를 반환
# print(list(dict1.keys())) #딕셔너리의 키를 반환
# print(dict1.values()) #딕셔너리의 값를 반환
# print(list(dict1.values()))
# print(dict1.items()) #key, value 쌍 얻기 (items) / 모두 지우기 = clear

############################################################################################################################################################
#집합 자료형 : 중복을 허용하지 않는다. 순서가 없다. 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형 / 중복된것은 모두 지우고 하나만 보여줌 page: 206
############################################################################################################################################################
#set 을 선언하는 법
s1 = set([1,1,22,2,2,2,3])
print(s1)

food = ['pho', 'noodle', 'pho', 'pho'] #list 형태
f = set(food)
print(f, type(f))
f.add("ramen") #추가
print(f, type(f))
f.update(['ramen2']) #전체에 추가
print(f, type(f))
#삭제
f.remove('ramen2')
print(f, type(f))

#중괄호 사용하면 set이 됨
mySet1 = {1,2,3,3,3,4}
print(mySet1)
yo = {1,2,3,3,3,4}
print(yo) 