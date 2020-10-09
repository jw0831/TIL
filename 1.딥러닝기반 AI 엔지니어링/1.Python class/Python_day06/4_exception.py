t = 0

if t == 1:

    try:
        a = int(input("a: "))
        b = int(input("b: "))

        c = a/b
        print("a/b = %d" % c) #something divide by 0 is not acceptable we need exception

    except:
        print("cannot divide by zero!")



if t == 2:
    try:
        a = int(input("a: "))
        b = int(input("b: "))

        c = a/b
        # print("a/b = %d" % c) #something divide by 0 is not acceptable we need exception

    except ZeroDivisionError as e:
        print("cannot divide by zero!")
    else:
        print("값은: %d" % c)

if t == 3:
    try:
        f = open("test.txt", "r", encoding='utf-8')
    except FileNotFoundError as e:
        f = open("test.txt", "w", encoding='utf-8')
        print("create a file")
    finally:
        f.close()

if t == 4:
    try:
        x = int(input("enter a number : "))
        y = int(input("enter anumber2 : "))
        z = x/y
    # except (ZeroDivisionError, ValueError):
    #     if ZeroDivisionError:
    #         print("Division by 0 not accepted")
    #     if ValueError:
    #         print("Out of allowed value")
    except ZeroDivisionError:
        print("Division by 0 not accepted")
    except ValueError:
        print("Out of allowed value")
    else:
        print("Division = ", z)
        print(x, y)
    finally:
            print("END")


#value error 를 인위적으로 발생시키고 싶을 때가 있다. 어떤 범위를 갑자기 초과하면
#따른 로직을 만들지 않더라도 value exception이 나오기때문에 그걸 잡아주면 된다.
''' 발생시키는법
raise
'''
happen = 0
if happen == 1:
    try:
        x = int(input("enter a number > 10: "))
        if x <= 10:
            raise ValueError #인위적으로 발생
    except ValueError:
        print("Error out of allowed range")
    else:
        print("Within allowed range")
    finally:
        print("end")
    
##############################################################################
#exercise
ex = 7
if ex == 1:
    import os
    try:
        os.remove('C:\\Temp\\noFile.exe')
    except:
        print("There is no file, please check!")

if ex == 2:
    myStr = "파이썬은 재미 있어요. 파이썬만 매일매일 공부하고 싶어요. ^^"
    strPosList = []
    index = 0

    while True:
        try:
            index = myStr.index("파이썬", index)
            strPosList.append(index)
            index = index + 1
        except:
            break
    
    print("파이썬 글자 위치 --> ", strPosList)

if ex == 3: #page 364
    num1 = input('숫자1 --> ')
    num2 = input('숫자2 --> ')
    
    try:
        num1 = int(num1)
        num2 = int(num2)
        num3 = num1 / num2
    except ZeroDivisionError:
        print("0으로 나눌수 없습니다.")
    except:
        print("오류가 발생했습니다.")
    else:
        print(num1, '/', num2, '=', num3)
    finally:
        print('이 부분은 무조건 나옵니다.')

if ex == 4:
    ss = 'Python is Easy. 그래서 programming이 재미있습니다. ^^'
    print(ss.swapcase())

if ex == 5:
    a, b = map(int, input().split())
    print(a+b)

if ex == 6:
    inStr = "  한글 Python 프로그래밍  "
    outStr = ""

    for i in range(0, len(inStr)):
        if inStr[i] != ' ':
            outStr += inStr[i]

    print("원래 문자열 ==>" + '[' + inStr + ']')
    print("공백 삭제 문자열 ==>" + '[' + outStr + ']')

#pg 231 self study 8-2 해보기
#Code08-04.py를 수정해서 '<<<파<<이>>썬>>>'이 '파이썬'으로 출력되도록 해 보자.
# 힌트 if 문이 '<'이 아닐때와 '>'이 아닐 때를 and로 연결해야 한다.
if ex == 7:
    inStr = "<<<파<<이>>썬>>>"
    outStr = ""

    for i in range(0, len(inStr)):
        if inStr[i] != "<" and inStr[i] != ">":
            outStr += inStr[i]

    print("원래 문자열 ==>" + '[' + inStr + ']')
    print("공백 삭제 문자열 ==>" + '[' + outStr + ']')

