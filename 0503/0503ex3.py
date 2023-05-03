'''
2023.05.03
고욱현
#문제정의
    1~입력받은 숫자까지의 합계 구하기
#문제분석
    변수 : num(입력받을 숫자)
#알고리즘
    1. 변수 선언 : num, total
    2. 논리 (반복)
        for i in range(1,num+1) :
'''

#for반복문
num=int(input('숫자 입력 : '))
total=0 #합계
for i in range(1,num+1) : #조건
    total = total + i #합계
print('1부터 {}까지의 합은 : {}'.format(num, total))

#while반복문
num = int(input('숫자 입력: '))
total = 0
i = 1
while i <= num:
    total = total + i
    i = i + 1
print('1부터 {}까지의 합은: {}'.format(num, total))

