'''
    2023.04.19
    고욱현  
    입력받은 숫자가 양수, 0, 음수인지 판단
    #문제분석
        변수-num
        수식
            num>0 양수
            num<0 음수
            num=0은 0
    #알고리즘
        1.변수선언
            num에 정수 입력
        2.논리 (선택)
            if num>0:
                print('입력값{}는 양수입니다'.format(num))
            if num<0:
                print('입력값{}는 음수입니다'.format(num))
            if num == 0 :
                print('입력값{}는 0입니다'.format(num))
'''

num=int(input('숫자 입력'))

if num>0:
    print('입력값{}는 양수입니다'.format(num))
if num<0:
    print('입력값{}는 음수입니다'.format(num))
if num == 0 :
    print('입력값{}는 0입니다'.format(num))