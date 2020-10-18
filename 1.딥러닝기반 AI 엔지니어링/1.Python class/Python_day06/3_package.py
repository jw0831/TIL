#module 여러개가 묶여있음.

#설정 관련 __init__.py 이걸 디폴트로 만들어줘야 인식이 가능함
'''
폴더를 만든다
MyApp -> mypackage -> __init__.py
                        greet.py
                        functions.py

'''
import sys
# print(sys.path) #환경변수 확인 하는법
# sys.path.append("C:\\MyApp") 
#import mypackage
# mypackage.functions.sub(1,2)

from mypackage import functions #package 에서 가져올때는 이렇게해야함
import mypackage.functions #이거도 됨.
print(functions.power(10,20))
from mypackage import greet
greet.sayHello(' kim')

from mypackage.functions import * #모두 불러 올때 aesterisk
print(functions.sub(40,20))
greet.sayHello(" both")

#from 모듈명 import 함수
#from 패키지명 import 모듈

#page 272

