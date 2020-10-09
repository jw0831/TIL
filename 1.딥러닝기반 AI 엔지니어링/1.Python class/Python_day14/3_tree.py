#http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html
# http://job.incruit.com/jobdb_info/jobpost.asp?job=2005280002846
# http://job.incruit.com/jobdb_info/jobpost.asp?job=2005280002846
# http://job.incruit.com/entry/jobpost.asp?job=2007210003505

#위 블로그처럼 깃허브로 APU모든 리포트 및 이력을 작성 할 것.
'''
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(4)
root.right.left = Node(5)
'''
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# data = [1,2,3,4,5]
root = Node(12)
root.insert(3)
root.insert(35)
root.insert(23)
root.insert(12)
root.insert(5)

