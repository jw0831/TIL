#리스트
'''a = [1, 'a', 'b', 'c', [1,2,3], ['a','b']]
print(a[0])
print(a[4])
print(a[4][2])
a[:3] = []
print(a)
del a[0]
print(a)
a.append([4,5,6]) #삽입
print(a)
a.insert(0, 1)
print(a)
a.insert(0, [5,6])
print(a)
print(a[0][1])
a.extend([4,5,6]) #항목이 추가된게 아니라 여러게가 붙어서 확장됨
print(a)
'''
#튜플
a = (1, 2, 'test', 'test2', 2.30)
print(a)
print(a[0])
print(a[:3])
