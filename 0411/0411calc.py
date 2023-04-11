'''
고욱현
2023.04.11
정수 2개를 입력받고 연산자 (+, -, *, /)중 하나를 입력받아서 수행하는 사칙연산 계산기
'''

num1 = int(input("정수를 입력해주세요 : "))
op = input("+, -, *, / 중 하나의 연산자를 입력해주세요 :")
num2 = int(input("정수를 입력해주세요 : "))


if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)

else :
    print("사칙연산자 중에서만 선택해주세요.")

print("수고하셨습니다.")