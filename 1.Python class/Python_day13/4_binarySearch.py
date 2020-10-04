'''
data = [2,4,7,8,9,10, 24, 1,4,5,3,2,2]
data.sort() # 바이너리 서치는 무조건 data가 정렬되어있어야함!
key = 7

low, high = 0, len(data) - 1 #index 값 찾는법
print(low, high)


while low <= high:
    mid = (low + high) // 2
    print(mid)

    if data[mid] == key: #일치하면 찾았다는 뜻
        print("found : ", mid)
        break
       
    if data[mid] > key:
        print("left : ", mid)
        high = mid - 1

    if data[mid] < key:
        print("right : ", mid)
        low = mid + 1

else:
    print("done")
'''

# https://blog.naver.com/bluebirdkids/220691361547 큐브 맞추는법

# 함수를 사용해서 변환하기

class binSearch():
    def __init__(self):
        self.data = []
        self.key = 0
    
    def search(self, data, key):
        self.data = data
        self.key = key
        self.data.sort()
        print(self.data)
        low, high = 0, len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            # print(mid)

            if self.data[mid] == self.key: #일치하면 찾았다는 뜻
                print("found : ", mid)
                break
            
            if self.data[mid] > self.key:
                print("left : ", mid)
                high = mid - 1

            if self.data[mid] < self.key:
                print("right : ", mid)
                low = mid + 1
        return data[mid]


bS = binSearch()
# data = [2,4,7,8,9,10, 24, 1,4,5,3,2,2]
ans = bS.search([2,4,7,8,9,10, 24, 1,4,5,3,2,2], 7)
print(ans)
