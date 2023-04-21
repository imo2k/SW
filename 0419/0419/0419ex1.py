'''
    2023.04.19
    고욱현
    문제풀이
        변수-성별(sex), 키(high), 몸무게(weight), 표준체중(avg)
        수식
            (남)avg=((high/100)**2)*22
            (여)avg=((high/100)**2)*21
    알고리즘
        1.변수선언
            sex, high, weight
        2. 논리(내포된 선택)
            if 성별이 남자 :
                avg계산
                if 119>=avg>=110
                    과체중
                elif avg>=120
                    비만
                else:
                    표준
            elif 성별이 여자 :
                avg계산
                if 119>=avg>=110
                    과체중
                elif avg>=120
                    비만
                else:
                    표준
            else :
                성별 잘못 입력
'''

sex=input("성별 입력 ('M or m 또는 F or f')")
high=float(input('키 입력'))
weight=float(input('몸무게 입력'))

if sex=='M' or sex=='m' :
    avg=((high/100)**2)*22
    if 119 >= weight/avg*100 >= 110 :
        print('과체중')
    elif weight/avg*100 >= 120 :
        print('비만 체중')
    else :
        print('정상체중')
elif sex=='F' or sex=='f' :
    avg=((high/100)**2)*21
    if 119 >= weight/avg*100 >= 110 :
        print('과체중')
    elif weight/avg*100 >= 120 :
        print('비만 체중')
    else :
        print('정상체중')
else :
    print('성별 입력이 잘못되었습니다.')
