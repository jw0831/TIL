################################################
# 파이썬은 모든게 이런식으로 작동한다. 
# Call by reference (in/out).
# 입출력 변수로 생각해도됨.
################################################
list1 = [1,2,3,4]
print(list1)

def change_list1(list2):
    list2.append(5)
    list2.append(6)
    print(list2)

def change_list2(list3):
    list3.append(8)
    list3.append(9)
    #print(list3)

change_list1(list1) #list2 = list1 이된다.
change_list2(list1)

print(list1)
################################################
def new_append(newList): #call by value
    newList = [2]
    print(newList)

new_append(list1)