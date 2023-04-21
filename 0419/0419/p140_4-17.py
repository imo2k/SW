'''
2023.04.19
고욱현
8세 이상이면서 120cm이상인 어린이 '고속 롤러코스터 입장 가능' 출력
8세 이상이면서 120cm미만인 어린이 '저속 롤러코스터 입장 가능' 출력
8세 미만인 어린이 '입장할 수 없습니다' 출력
#문제분석
    변수 : 나이(age), 키(tall)
    수식 : age >= 8 and tall >= 120
    age >= 8 and tall < 120
#알고리즘
    변수선언 : age = int(input("나이 입력 : "))
             tall = int(input("키 입력(cm) : "))

    논리 (선택 if-반복문)
        if age>= 8:

            tall = int(input("키 입력(cm) : "))
            if tall >= 120 :
                print("고속 롤러코스터 입장 가능.")
            else :
                print("저속 롤러코스터 입장 가능.")
        else :
            print("입장할 수 없습니다.")
'''

age = int(input("나이 입력 : "))


if age>= 8:

    tall = int(input("키 입력(cm) : "))
    if tall >= 120 :
        print("고속 롤러코스터 입장 가능.")
    else :
        print("저속 롤러코스터 입장 가능.")
else :
    print("입장할 수 없습니다.")