#다음의 데이터를 bubble sort를 하고 binary search를 하여 결과값이 있는지 검색하시오.

data = [20,1,3,10,12,18,21,100] #len = 8
key = 12

for sort in range(len(data)-1,0,-1): #7 6 5 4 3 2 1
    # print(sort)
    for bubble in range(sort): #0~6 = 7개
        # print(bubble)
        if data[bubble]>data[bubble+1]: #6+1 해주니까 7까지 비교를 해줌
            temp = data[bubble+1]
            data[bubble+1] = data[bubble]
            data[bubble] = temp

# print(data) #data is sorted

#now time for binary search

def binarySearch(data, key, high, low):
    mid = low + (high-low)//2
    if high>=low:
        if data[mid] == key:
            print("key {} match with data index {}".format (key, mid))
            return True
        elif data[mid] > key:
            return binarySearch(data, key, mid-1, low)
        else:
            return binarySearch(data, key, high, mid+1)
    else:
        print("does not match")
        return False
low, high = 0, len(data)-1
print(binarySearch(data, key, high, low))