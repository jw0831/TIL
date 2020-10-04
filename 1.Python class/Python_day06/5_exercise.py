'''
#(저장은 txt 파일로 한다.)
# 회원관리
#########################
 1. 전체회원검색
 2. 회원검색
 3. 회원추가
 4. 회원수정
 5. 회원삭제
 6. 종료
#########################
메뉴를 선택해주세요.(1-6):

* 다음 메뉴를 구성하고 회원을 관리할수 있도록 처리한다.
단, txt파일 형태로 관리한다. 회원은 중복되지 않는다.
Class를 사용하여 구현하시오. 안된다면 Functions을 사용하여 구현하시오.
저장 파일은 users.txt
users.txt의 구성 
이순신
홍길동
권율
강감찬
refer pg 333, 334, 335, 336
'''
#########################-import-########################
import time
#########################회원 파일 생성########################
#처음 한번
dataList = ["이순신\n", "홍길동\n", "권율\n", "강감찬\n"]
inFp = open("C:\\PythonTest\\Python_day6\\client.txt", "w", encoding="UTF-8")
for i in dataList:
    inFp.write(i)
        
inFp.close()
print("Initial client list has been created")
#########################변수 지정########################

#######################클래스 만드는곳####################



#######################함수 만드는곳######################



##########################메인###########################
while True:
    print("#회원관리")
    print("#########################")
    print(" 1. 전체회원검색")
    print(" 2. 회원검색")
    print(" 3. 회원추가")
    print(" 4. 회원수정")
    print(" 5. 회원삭제")
    print(" 6. 종료")
    print("#########################")

    client = input("원하시는 서비스를 선택하세요: ")

    if client == '1':
        inFp = None
        dataList, dataStr = [], ""

        inFp = open("C:\\PythonTest\\Python_day6\\client.txt", "r", encoding="UTF-8")

        dataList = inFp.readlines()
        for dataStr in dataList:
            print(dataStr, end = "")

        inFp.close()
    elif client == '2':
        check = 0
        look4Client = str(input("찾으려는 회원명을 입력 하시오: "))
        inFp = open("C:\\PythonTest\\Python_day6\\client.txt", "r", encoding="UTF-8")
        # print(inFp.readlines()) #['이순신\n', '홍길동\n', '권율\n', '강감찬\n']
        for line in inFp.readlines():
            if line.replace("\n","") == look4Client:
                check = 1
                break
        if check == 1:
            print("%s 님이 존재합니다." % look4Client)
        else:
            print("%s 님이 존재하지 않습니다." %look4Client)
    elif client == '3':
        pass
    elif client == '4':
        pass
    elif client == '5':
        pass
    elif client == '6':
        print("시스템을 종료합니다.")
        time.sleep(1)
        break
    else:
        print("잘못 입력하셨습니다.")
        time.sleep(1)
