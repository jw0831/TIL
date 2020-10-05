#다음의 Stack 클래스의 함수를 구현하시오. stack 은 LIFO임.
#항상 스택의 마지막 PUSH 데이터에 대한 포인터를 유지함. 이 포인터는 항상 스택의 top,
#따라서 이름이 나타내는 것처럼 top 포인터는 스택의 상단위에 값을
#가르켜야하고 실테로 삭제하지 않음
#비동기 동기처리 / 객체지향적 에 대해 설명해주세요 (인터뷰) 물어보는 내용.. 10분정도 프레젠테이션 

class Stack:
    def __init__(self):
        # self.item = 0
        self.point = 0
        self.box = []
        
    def isEmpty(self): #스택이 비어 있는지 확인
        if len(self.box) == 0:
            e = 'empty'
            return e
        else:
            ne = "not empty"
            return ne
    def push(self, item): #스택에서 요소를 푸시(저장)함.
        self.item = item
        pu = self.item
        cabinet = self.box
        cabinet.append(pu)
        print(cabinet)
        return cabinet

    def pop(self): #스택에서 요소를 제거(액세스)함.
        pass
    def peek(self): #스택의 최사위 데이터 요소를 제거하지 않고 가져옴
        pass
    def getItems(self):
        pass

st = Stack()
isE = st.isEmpty()
print(isE)
p = st.push(12)
print(p)
p = st.push(32)
print(p)
p = st.push(52)
print(p)
isE = st.isEmpty()
print(isE)
# po = st.pop()
# print(po)
# pe = st.peek()
# print(pe)