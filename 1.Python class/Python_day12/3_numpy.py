import numpy as np

#1 차원 배열
# d = np.array([1,2,3,4])
# print(d)

# #2 차원 배열
# d2 = np.array([[1,2,3,4],[2,3,4,6],[5,6,8,9]])
# print(d2)
# print(d2[0])
# print(d2[0][1])

# print(d2.shape) #차원 dimension

# from numpy import *
# d2 = np.array([[1,2,3,4],[2,3,4,6],[5,6,8,9]])
# print(d2.shape)
# print(reshape(d2,(4,3))) # (4,3)

#여러개를 합쳐서 데이터를 사용하는것을 콜랙션 
#int 같은 하나만 사용하는것은 콜랙션이 아니다.




#Chain map 유용함
import collections #여기에 chain map 콜랙션 이 있음
d3 = {'day1': 'mon', 'day2': 'tue'}
d4 = {'day3': 'wed', 'day4': 'tur'} #이렇게 묶어주는게 체인맵

r = collections.ChainMap(d3, d4)

print(r)
print(r.maps, "\n")
print(list(r.keys()), list(r.values()))

