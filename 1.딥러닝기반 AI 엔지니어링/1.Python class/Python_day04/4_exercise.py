#구구단의 결과를 text 파일에 나타내시오
f = open("C:\\PythonTest\\Python_day4\\text.txt", "w", encoding="UTF-8") #인코딩 방식 한글 추가 가능
f.write("-------------\n")
title = ("구구단\n")
f.write(title)
f.write("-------------\n")

for i in range(2,10):
    enter = ("\n")
    f.write(enter)
    f.write("%d 단\n" %i)

    for j in range(1,10):
        data = ("{} x {} = {}\n" .format(i, j, i*j))
        f.write(data)
        # print(end="\n")
        
f.close()


# i = 100000
# print("여기%10d" % i)