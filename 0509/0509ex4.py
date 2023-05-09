'''
2023.05.09
고욱현
#문제정의
    1~100까지의 입력받은 숫자의 배수의 합계
#문제분석
    변수 : 정수(num), 반복변수(i), 합계(total)
##알고리즘
    1. 변수 초기화
        num변수에 정수 입력
        i = 0
        total = 0
    2.  프로그램 논리(반복 while)
        while i < 100:
            if i % num == 0:i += 1
            if (i % num) != 0 :
                continue
            total += i
'''

num = int(input("합을 원하는 배수 입력 :"))
i = 0
total = 0

while i < 100:
    i += 1
    if (i % num) != 0 :
        continue
    total += i
print("1부터 100까지 {}의 배수의 합은 : {}".format(num, total))
