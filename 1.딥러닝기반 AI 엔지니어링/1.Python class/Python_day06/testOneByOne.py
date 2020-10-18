test = 4

dataList = ["이순신\n", "홍길동\n", "권율\n", "강감찬\n"]
# dataList = ["이순신", "홍길동", "권율", "강감찬"]
dataStr = ""
if test == 1:
    
    f = open("C:\\PythonTest\\Python_day6\\client.txt", "w", encoding="UTF-8")
    for i in dataList:
        f.write(i)
        print(i)
    f.close()

elif test == 2: 
    for i in dataList:
        print(i,type(i))

elif test == 3:
    inFp = None
    lineList, lineStr = [], ""

    inFp = open("C:\\PythonTest\\Python_day6\\client.txt", "r", encoding="UTF-8")

    lineList = inFp.readlines()
    for lineStr in lineList:
        print(dataStr, end = "")

    inFp.close()

elif test == 4: #회원 검색
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

    # lines = inFp.readlines()
    # # for dataStr in dataList:
    # if dataStr == look4Client:
    #     print(look4Client)
    # else:
    #     print("회원이 존재하지 않습니다.")



'''
f = open("test.txt", "w", encoding='UTF-8')
f.writelines("test")
f.writelines("test")
f.close()
print("file saved")

f2 = open("test.txt", "r", encoding='UTF-8')
print(f2.readlines())
#['test\n', 'test2\n'] 이런식으로 들어갈 경우
for line in f2.readliens():
    print(line) #test\n
    if line.replace("\n","") == '홍길동':

print(line.replace("\n","")) 


check = False
for line in f2.readlines():
    #print(line.replace("\n","")) #test\n
    #if line.replace("\n","")
    if line == '홍길동':
        check = True
        break

if check:
    print("홍길동이 존재 합니다.")
else:
    print("홍길동이 존재하지 않습니다.")


******* 클래스 *******
class clientSupervise:

    def addClient():

    def deleteClient():



'''