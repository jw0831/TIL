class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

inorder(r)

#             50
#     30              70
# 20      40      60      80

 #재귀 함수등 알고리즘 책을 사서 공부하고 코딩테스트 공부
#회사 코딩테스트 올림피아 처럼 
# 알고리즘 이런거에서 루프 사용해서 로직을 만들줄 알면됨. 
# https://sueaty.tistory.com/40 
# 기초 : 코드업(알고리즘을 처음 접하는 학생이 쉽게 시작할 수 있는 기초 100제)
# 그 이후: 백준, 코드포스 등의 사이트에서 문제를 풀어보는 것이 좋음
# 삼성전자 역량 테스트 기출은 백준에서 전부 확인 가능
# 카카오 코딩 테스트는 프로그래머스 사이트에 게시되어 있음
# https://programmers.co.kr/learn/challenges?utm_source=google&utm_medium=cpc&utm_campaign=coding_test&gclid=EAIaIQobChMI64imtJL06gIVCFVgCh05xA37EAAYASABEgIHIfD_BwE
# 비즈니스와 기술을 함께 가져갈수 있는 회사로 가야한다.

