#다음의 클래스와 함수를 구현하시오.
class LinearSearch:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        # print(self.data)
        # print(self.key)

    def getSearchExist(self): #--> 존재유무(True, False)
        check = False
        for i in range(len(self.data)):    
            if self.data[i] == self.key:
                check = True
        return check

    def getSearchCount(self): #--> 개수반환(2)
        counter = 0
        for i in range(len(self.data)):    
            if self.data[i] == self.key:
                counter += 1
        return counter

    def getSearchElements(self): # -> [3,3]
        newData = list()
        for i in range(len(self.data)):    
            if self.data[i] == self.key:
                newData.append(self.data[i]) 
        return newData

    def getSearchIndexes(self): # -> [1,3]
        j = list()
        for i in range(len(self.data)):    
            if self.data[i] == self.key:
                j.append(i)
        return j

    #teacher
    # def getSearchIndexes(self): # -> [1,3]
    #     self.temp2 = {}
    #     self.index = 0
    #     for self.value in self.data:
    #         self.temp2[self.index] = self.value
    #         self.index += 1

    #     self.temp3 = []
    #     for self.index, self.value in self.temp2.items():
    #         if self.value == self.key:
    #             self.temp3.append(self.index)
    #     return self.temp3

run = LinearSearch([10,3,1,3,3,3], 3)
exist = run.getSearchExist()
# print(exist)
count = run.getSearchCount()
# print(count)
element = run.getSearchElements()
# print(element)
inde = run.getSearchIndexes()
print(inde)
