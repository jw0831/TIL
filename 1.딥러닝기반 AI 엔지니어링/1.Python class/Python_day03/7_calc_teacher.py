# 사칙연산을 계산할수 있는 계산기를 구현하시오.(두수의 사칙연산.)
# (단, 함수를 사용하여 구현할 것, 종료하기전까지 계속 처리됨.)
###########################
# 1. 덧셈
# 2. 뺄셈
# 3. 곱셈
# 4. 나눗셈
# 5. 종료 
##########################
# 선택해주세요.(1-5) :

import time

def inputs():
	num1 = int(input("첫번째 숫자를 입력해주세요. :"))
	num2 = int(input("두번째 숫자를 입력해주세요. :"))
	return num1, num2

def calculate(op, num1, num2):
	if op == "+":
		return num1 + num2
	elif op == "-":
		return num1 - num2
	elif op == "*":
		return num1 * num2
	elif op == "/":
		return num1 / num2

while True:
	print("#############################")
	print("# 1. 덧셈                    ")
	print("# 2. 뺄셈                    ")
	print("# 3. 곱셈                    ")
	print("# 4. 나눗셈                  ")
	print("# 5. 종료                    ")
	print("#############################")
	sel = input("선택해주세요.(1-5) :")

	if sel == "1":
		nums = inputs()
		x, y = nums[0], nums[1]
		result = calculate("+", x, y)
		print("{} + {} = {}".format(x, y, result))
		time.sleep(1)

	elif sel == "2":
		nums = inputs()
		x, y = nums[0], nums[1]
		result = calculate("-", x, y)
		print("{} - {} = {}".format(x, y, result))
		time.sleep(1)

	elif sel == "3":
		nums = inputs()
		x, y = nums[0], nums[1]
		result = calculate("*", x, y)
		print("{} * {} = {}".format(x, y, result))       
		time.sleep(1)

	elif sel == "4":
		nums = inputs()
		x, y = nums[0], nums[1]
		result = calculate("/", x, y)
		print("{} / {} = {}".format(x, y, result))
		time.sleep(1)        

	elif sel == "5":
		print("감사합니다. 안녕히 가십시오.")
		time.sleep(1)
		break

	else:
		print("잘못선택하셨습니다.")
		time.sleep(1)