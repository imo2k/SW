'''
2023.04.12
고욱현
두 개의 숫자를 입력받아 
모두 짝수이면 "모두 짝수" 출력
모두 홀수이면 "모두 홀수" 출력
아니면 "홀수, 짝수 섞여 있음" 출력

#문제분석
    변수 - 정수1(num1), 정수2(num2)
    수식 - 정수1이 짝수 (num1%2==0), 정수1이 홀수 (num1&2==1)
           정수2가 짝수 (num2%2==0), 정수2가 홀수 (num2&2==1)

#알고리즘
    1. 변수선언
        num1 = int(input("첫 번째 숫자 입력"))
        num2 = int(input("두 번째 숫자 입력"))
    2. 논리 (선택 if-elif-else)
        if num1%2==0 and num2%2==0 :
            (조건 1 참일 경우), "모두 짝수"
        elif num1%2==1 and num2%2==1 :
            (조건 2 참일 경우), "모두 홀수"
        else :
            "홀수, 짝수 섞여있음"
'''

num1 = int(input("첫 번째 숫자 입력 : ")) # 첫 번째 정수 입력
num2 = int(input("두 번째 숫자 입력 : ")) # 두 번째 정수 입력

if num1%2==0 and num2%2==0 : # 조건 1
    print("두 숫자가 모두 짝수입니다.") # 조건 1 참일 경우
elif num1%2==1 and num2%2==1 : # 조건 2 (조건 1이 거짓일 경우)
    print("두 숫자가 모두 홀수입니다.") # 조건 2 참일 경우
else :
    print("홀수, 짝수가 섞여 있습니다.") # 조건 1, 2가 거짓일 경우