#사칙연산을 계산할수 있는 계산기를 구현하시오. (두수의 사칙연산.)
#(단, 함수를 사용하여 구현할 것, 종료하기 전까지 계속 처리됨.)
num1 = 0
num2 = 0

def sum(num1, num2):
    print("Addition")
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))
    result = num1 + num2
    print("{} + {} = {}".format(num1,num2,result))
    return result

def sub(num1, num2):
    print("Substraction")
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))
    result = num1 - num2
    print("{} - {} = {}".format(num1,num2,result))
    return result

def mul(num1, num2):
    print("multiplication")
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))
    result = num1 * num2
    print("{} x {} = {}".format(num1,num2,result))
    return result

def div(num1, num2):
    print("Division")
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))
    result = num1 / num2
    print("{} / {} = {}".format(num1,num2,result))
    return result

while True:
    print("====================")
    print("*****Calculator*****")
    print("====================")
    print("# 1: Addition")
    print("# 2: Substraction")
    print("# 3: Multiplication")
    print("# 4: Division")
    print("# 5: End")
    print("====================")
    num = input("Your choice (1~5) : ")
    if(num == "1"):
        sum(num1, num2)

    elif(num == "2"):
        sub(num1, num2)

    elif(num == "3"):
        mul(num1, num2)

    elif(num == "4"):
        div(num1, num2)
        
    elif(num == "5"):
        print("end")
        break
    else:
        print("wrong input")