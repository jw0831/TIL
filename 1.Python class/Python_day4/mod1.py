#module
def sum(a,b):
    return a + b

#여기에 코드 작성하면 import할때 보인다.. 중대한 문제...!!!
#파이썬은 .py 이면서 실행 프로그램이기 때문에
# 아래 __ 내부 변수 이다.  내부변수를 작성해 줌으로써 모듈로 사용되면 아래 단독 프로그램은 실행이 되지 않는다.
if __name__ == "__main__": #2_module.py 에서는 mod1.py가 모듈로 불러왔을때 작동 안함
    print("module", sum(8,1))