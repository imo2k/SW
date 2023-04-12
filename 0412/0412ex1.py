'''
2023.04.12
고욱현
평점을 입력받아서 평점 출력, 4.2점 이상이면 "해외연수"

#문제분석
    변수 - 평점(score)

#알고리즘
    1. 변수선언
        score에 평점 실수로 입력하기
    2. 논리(선택)
        if score >= 4.2 :
            print("해외연수 기회 부여")
'''

score = float(input("Enter your score : "))

if score >= 4.2 :
    print("당신의 평점은 : ", score)        
    print("해외연수 기회 부여")
'''
else :
    print("아쉽지만 다음에 또 지원해주세요.")
    print("수고하셨습니다.")
'''
