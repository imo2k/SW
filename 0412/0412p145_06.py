'''
2023.04.12
고욱현
p145 6번

#문제분석
    변수 - 정수1(num1), 정수2(num2), 짝수일 경우의 더한 결과값(result)
    수식 - num1%2==0 and num2%2==0 (정수1, 정수2 모두 짝수)
          num1%2==1 and num2%2==0 (정수1 홀수 정수2 짝수)
          num1%2==0 and num2%2==1 (정수1 짝수 정수2 홀수)

#알고리즘
    1. 변수선언
        num1 = int(input("첫 번째 정수를 입력하세요 :"))
        num2 = int(input("두 번째 정수를 입력하세요 :"))
    2. 논리(선택, if-elif-else)
        if num1%2==0 and num2%2==0
            조건 1 : 모두 짝수인 경우
        elif num1%2==1 and num2%2==0 :
            조건 2 : num1만 홀수인 경우
        elif num1%2==0 and num2%2==1 :
            조건 3 : num2만 홀수 인 경우
        else :
            모두 홀수인 경우
'''

num1 = int(input("첫 번째 정수를 입력하세요 :")) # 첫 번쨰 정수 입력
num2 = int(input("두 번째 정수를 입력하세요 :")) # 두 번쨰 정수 입력

if num1%2==0 and num2%2==0 : # 조건 1(모두 짝수일 경우)
    print(num1, "+", num2, "=", num1+num2)
elif num1%2==1 and num2%2==0 : # 조건 2 (num1만 홀수인 경우)
    print("첫 번째 정수를 짝수로 입력하세요.")
elif num1%2==0 and num2%2==1 : # 조건 3 (num2만 홀수인 경우)
    print("두 번째 정수를 짝수로 입력하세요.")
else : # 모두 홀수인 경우
    print("두 숫자 모두를 짝수로 입력하세요.")