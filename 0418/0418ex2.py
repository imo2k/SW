'''
2023.04.18
고욱현
두 과목 모두 75점 이상 그리고 총점 180점 이상 "최우수",
총점 160점 이상 "우수", 150점 이상 "보통"
두 과목 모두 75점 미만이면 "분발합시다."
#문제 분석
    변수 : 점수 1(score1), 점수 2(score2), 합계 (total)
#알고리즘
    1. 변수 선언
        score1, score2에 점수 입력 받기
    2. 논리(선택-중첩if문)
        if score1 >= 75 and score2 >= 75 :
            if (total) >= 180
                "최우수"
            elif (total) >= 160 :
                "우수"
        else :
            "보통"
    else :
        "분발합시다."
'''

score1 = int(input("점수 입력 : "))
score2 = int(input("점수 입력 : "))

total = score1 + score2

if score1 >= 75 and score2 >= 75 : #조건 1
    if total >= 180: #조건 2-1
        print("최우수") #조건1, 조건2-2, 모두참
    elif total >= 160 : #조건 2-2
        print("우수") #조건1, 조건2-2 모두 참
    else :
        print("보통") #조건1 참, 조건2-1,2-2 모두 거짓
else : 
        print("분발합시다.") #조건1 거짓