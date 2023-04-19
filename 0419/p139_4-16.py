'''
2023.04.19
고욱현
p.139 실습 예제 4-16
직급과 나이를 입력받아 직금이 7 또는 8급이고 나이가 40대(40~49)이면 '연금 80% 대상자입니다'
직금이 5 또는 6급이고 나이가 50대(50~59)이면 '연금 100% 대상자입니다.출력
그 외의 경우는 '연금 대상자가 아닙니다' 출력
문제 분석
    변수 : 직급(rank), 나이(age), 
    수식 : age >= 40 and age < 50 and rank = 7 or 8
          age >= 50 and age < 60 and rank = 5 or 6

알고리즘 
    변수 선언 : rank = int(input("직급 입력 : "))
              age = int(input("나이 입력 : "))

    논리(선택-반복if문)
        if (rank == 7 or rank == 8) and age >= 40 and age <= 49:
          elif (rank == 5 or rank == 6) and age >= 50 and age <= 59:
          else:
'''

rank = int(input("직급 입력 : "))
age = int(input("나이 입력 : "))

if (rank == 7 or rank == 8) and age >= 40 and age <= 49:
    print("연금 80% 대상 자입니다.")
elif (rank == 5 or rank == 6) and age >= 50 and age <= 59:
    print("연금 100% 대상 자입니다.")
else:
    print("연금 대상자가 아닙니다.")
