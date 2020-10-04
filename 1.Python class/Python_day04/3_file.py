f = open("C:\\PythonTest\\Python_day4\\text.txt", "w") 
'''
'r' open for reading (default) 
'w' open for writing, truncating the file first 
'x' create a new file and open it for writing 
'a' open for writing, appending to the end of the file if it exists 
'b' binary mode 
't' text mode (default) 
'+' open a disk file for updating (reading and writing)
'''
ex = 0
if ex == 1:
    for i in range(1, 11):
        data = "%d 번째 데이터.\n" % i
        f.write(data)
    f.close()
##############################################################
elif ex == 2:
    f2 = open("C:\\PythonTest\\Python_day4\\text.txt", "r")
    #print(f2.readline())
    while True:
        line = f2.readline()
        if not line: break
        print(line)
    f2.close()
##############################################################
elif ex == 3:
    f3 = open("C:\\PythonTest\\Python_day4\\text.txt", "r")
    lines = f3.readlines()
    print(lines) #list 로 나오는 것을 확인할 수 있다.
    #그러므로 for 구문을 쓰면 위에 while처럼 된다.
    for line in lines:
        print(line)
##############################################################
elif ex == 4:
    f4 = open("C:\\PythonTest\\Python_day4\\text.txt", "a")
    for i in range(11,31):
        data = "%d 번째 입력 \n" % i
        f4.write(data)
    f4.close()

    fl = 0
####################### code 11-04.py / text파일의 스트링을 리스트 형태로 인식해서 스트링을 하나씩 따오는것
if fl == 1:
    inFp = None
    inList, inStr = [], ""

    inFp = open("C:/Temp/data1.txt", "r")

    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end = "")

    inFp.close()
######################################
#application programming interface (API)
