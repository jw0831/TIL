#다음에 제공되는 데이터에 갑이 존재하는지 검색하시오.
#결과는 True, False

# element = [10,2,3,4,5,5,3]
# i = 0
# def searchElement(data):
#     for i in range(0, len(element)):
#         if data == element[i]:
#             print("True")
#         else:
#             print("False")


# # searchElement([10,2,3,4,5,5,3]) #-> True
# # searchElement([10,2,3,4,5],6) #-> False
# #in 사용하지 않고 하기

# s = searchElement(2)
#################################################

# element = [10,2,3,4,5,5,3]
# # i = 0
# # print(len(element))
# def searchElement(data):
#     sw = 0
#     for i in range(0, len(element)):
#         if data == element[i]:
#             # print("True")
#             sw = 1
#     if sw == 0:
#         # print("False")
#         return False
#     if sw == 1:
#         # print("True")        
#         return True        


# # searchElement([10,2,3,4,5,5,3]) #-> True
# # searchElement([10,2,3,4,5],6) #-> False
# #in 사용하지 않고 하기

# s = searchElement(4)
# print(s)

#################################################
# teacher's
data = [10,2,3,4,5,5,3]
# i = 0
# print(len(element))
def searchElement(data, key):
    check = False
    for i in range(len(data)):
        if data[i] == key:
            check = True
    return check

# r = searchElement(data, 2)
r = searchElement([10,2,3,4,5,5,3], 3)
print(r)
print(searchElement([1,43,3,4,5],2))