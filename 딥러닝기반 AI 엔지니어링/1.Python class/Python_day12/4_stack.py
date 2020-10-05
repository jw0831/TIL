'''
#stack 스텍
temp = []
temp.append('a')
temp.append('b')
temp.append('c')
print(temp)
temp.pop()
print(temp)
print("이런걸 LIFO (Last In First Out)이라고 한다. 후입선출")
'''

# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, v):
#         self.stack.append(v)
#     def pop(self):
#         return self.stack.pop()
#     def peek(self):
#         return self.stack[-1]


# s= Stack()
# s.push(1)
# s.push(2)
# print(s.pop())
# print(s.pop())

#queue
#first in first out
# 모바일 통신사에서 데이터를 전송했는데 누군가의 폰 전원이 셧다운 되었지만 처음보낸 정보가 폰이 켜지고 잠시후에 먼저 전송 된다.
class Queue:
    def __init__(self):
        self.queue = list() #[] 와 같다.
    def insert(self,value):
        self.queue.insert(0, value) #insert 를 통해서 삽입 위치를 0 번으로 지정함으로써 왼쪽에서 넣어주니까 나중에 pop을 사용할때 FIFO가 가능하게 해준다.
        print(self.queue, type(self.queue))
    def size(self):
        return len(self.queue)
    def remove(self):
        return self.queue.pop()

q = Queue()
q.insert('Mon')
q.insert('Tue')
q.insert('Wed')
# print(q.size())
print(q.remove())
print(q.remove())

