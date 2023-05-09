'''
2023.05.09
고욱현
#문제정의
    입력받은 숫자의 팩토리얼 값 계산하기
#문제분석
    변수 : 정수(num), 팩토리얼(fac)
#알고리즘
    1. 변수 초기화
        num변수에 정수 입력
        fac = 1
    2. 프로그램 논리(반복 for)
        for i in range(num, 0, -1)
            fac = fac * i
'''

num = int(input("팩토리얼 숫자 입력 : "))
fac = 1

for i in range(num, 0, -1) : #반복 조건
    fac = fac * i #팩토리얼 계산
#print("{}의 팩토리얼 값은 : {}".format(num, fac))
print("%d의 팩토리얼 값은 : " %num, fac) # 변수를 표시할 자리에 정수형의 데이터 타입을 표시할 때 %d를 사용 (형식 지정자)
                                     # %f 실수형
