#사칙연산을 계산할수 있는 계산기를 구현하시오. (두수의 사칙연산.)
#(단, 함수를 사용하여 구현할 것, 종료하기 전까지 계속 처리됨.)

##############################함수#############################
def getNum():
    global num1
    global num2
    num1 = 0
    num2 = 0
    num1 = int(input("Input your 1st Number: "))
    num2 = int(input("Input your 2nd Number: "))
    return

def sum(num1, num2):
    print("Addition")
    result = num1 + num2
    print("{} + {} = {}".format(num1,num2,result))

def sub(num1, num2):
    print("Substraction")
    result = num1 - num2
    print("{} - {} = {}".format(num1,num2,result))

def mul(num1, num2):
    print("multiplication")
    result = num1 * num2
    print("{} x {} = {}".format(num1,num2,result))

def div(num1, num2):
    print("Division")
    result = num1 / num2
    print("{} / {} = {}".format(num1,num2,result))
    
###############################################################
#변수는 전역 처리됨 
###############################################################
#메인
###############################################################
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
        getNum()
        sum(num1, num2)

    elif(num == "2"):
        getNum()
        sub(num1, num2)

    elif(num == "3"):
        getNum()
        mul(num1, num2)

    elif(num == "4"):
        getNum()
        div(num1, num2)
        
    elif(num == "5"):
        print("end")
        break
    else:
        print("wrong input")
    ###############################################################