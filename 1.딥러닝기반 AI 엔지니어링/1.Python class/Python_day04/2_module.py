'''
#파이썬에서 제공되는 환경변수에 들어가 있으면, 다른 경로에 있더라도 호출 가능..
#환경변수를 세팅 하면됨.
#폴더를 따로 만들어서 파이썬의 환경변수에 경로를 추가 및 설정 해주면 된다.
'''

selMod = 2
run = 2

#run = int(input("Your choice: "))
if selMod == 1:
    import mod1 as m

elif selMod == 2:
    import sys #여기에 PATH 라는것이 있음.
    sys.path.append("C:\\MyPythonModule") #\를 \\로 바꿔야함   : 1. 이렇게 추가를 해준 상태에서 
    print(sys.path)
    # ['c:\\PythonTest\\Python_day4', 'C:\\Python37\\python37.zip', 
    # 'C:\\Python37\\DLLs', 'C:\\Python37\\lib', 'C:\\Python37', 
    # 'C:\\Users\\i\\AppData\\Roaming\\Python\\Python37\\site-packages', 
    # 'C:\\Python37\\lib\\site-packages'] - 오리지널 경로..

    #import mod_path_changed as wow  #2. 추가를 해주면 된다.

elif selMod == 3:
    #시스탬 고급 시스템 설정에서 환경변수 에서 시스템변수에 PATH 추가 해주면 된다.
    #['c:\\PythonTest\\Python_day4', 'C:\\Python37\\python37.zip', 'C:\\Python37\\DLLs', 
    # 'C:\\Python37\\lib', 'C:\\Python37', 'C:\\Users\\i\\AppData\\Roaming\\Python\\Python37\\site-packages', 
    # 'C:\\Python37\\lib\\site-packages', 
    #'C:\\MyPythonModule'] #시스탬 변수에 추가한 경로 이름이 추가된걸 위에 selMod 2번의 sys.path 읽기 기능으로 확인할수 있다.
    import mod1 as wow

elif selMod == 4:
    pass

elif selMod == 5:
    pass
else:
    pass


if run == 1:
    
    a = wow.sum(1,2)
    print(a)

elif run == 2:
    pass

elif run == 3:
    pass

elif run == 4:
    pass

elif run == 5:
    pass
else:
    pass