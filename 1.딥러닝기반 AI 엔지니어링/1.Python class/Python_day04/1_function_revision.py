########################################################
'''
def add_substract_multiple_divide(a, b):
    return a+b, a-b, a*b, a/b

print(add_substract_multiple_divide(4,5), type(add_substract_multiple_divide(4,5)))
result = add_substract_multiple_divide(4,5)

for item in result: #tuple 이니까 for 로 갯수만큼 루틴으로 돌려서 사용 가능
    print(item, end=" ")
'''
########################################################
#call by value(only input)
#call by reference(input / output)
'''
pip install ipython #누르면 자동을 체크가 되는~ cmd 에서 설치 / cls 창 클리어
'''
run = 6

if run == 1:
    a = 1
    def test(x):
        x = 20
        return x

    test(a)
    print(a) #a = 그대로 있고
    print(test(a)) #a 와 test(x) 가 따로 존재한다.

elif run == 2:
    l = [1,2,3]
    def test2(j): # j = l : reference를 넘겨서 계속 사용하는 것이다. 리스트만 해당된다.. 튜플은 추가가 안되니..
        j.append(4)
#리스트는 배열(array)같은것에도 많이 사용된다...
    test2(l)
    print(l) #j 를 통해 append 하였으니 j 와 l 이 같이 존재한다.

elif run == 3:
    l = [1,2,3]
    def test2(j): 
        j = [1,2,2]

    test2(l)
    print(l) #l 에는 변화가 없다. 

#################그러므로 위의 예제를 통해보면 아래 4번에서 밖에 a = 1과 안에 들어간 a 와 서로 다르다...
elif run == 4:
    a = 1
    def vartest(a):
        a = a + 1  #이 a 는 안에서만 사용된다...!!! 안에서는 2지만 밖에서는 1이다.
        # print(a)
        return a
    
    print(a)
    print(vartest(a))
    
elif run == 5:
    a2 = 1 #변수 설정을 미리 해주어야 함수안에서 전역변수 지정가능 
    def vartest2():
        global a2
        a2 = a2 + 1

    vartest2()
    print(a2)

elif run == 6: #lambda
    add = lambda x, y: x + y
    result = add(10,20)
    print(result)

    def testfunc(a):
        result3 = a(20, 30) #변수 말고 함수도 받고 있다라는 말.
        print(result3)

    testfunc(add) #a = add 위에 람다식에 있던 변수가 함수가 되어버림

elif run == 7: #lambda
    pass
