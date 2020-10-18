data = [20,1,3,10,12,18,21,10]
# print(len(data)) #8
def insertSort(data):
    for index in range(1, len(data)):
        # print(index, end='')
        currentvalue = data[index]
        position = index
        # print(position, ", ", currentvalue)
        while position >0 and data[position-1] > currentvalue: #key point 1
            data[position] = data[position-1]
            position = position - 1
            print(position, ", ", position-1)
        data[position] = currentvalue #key point 2

insertSort(data)
# print(data)

