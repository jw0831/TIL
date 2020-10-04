def add(a,b):
    return a + b

#method 1
c = add(1,2)
print(c)
#method 2
c2 = add
c3 = c2(1,2)
print (c3)
#method 3
c4 = lambda x,y: x+y
c5 = c4(1,2)
print(c5)
#method 4
def test(f,data):
    result = f(data[0],data[1])
    return result

r = test(lambda x,y:x+y,[1,2]) #자연스럽게 사용할줄 알아야함
print(r)

