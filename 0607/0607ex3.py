'''
2023.06.07
고욱현
#문제정의
    5명의 학생의 학번, 전화번호를 입력 받아 딕셔너리에 저장
    학번으로 전화번호 검색하기
#문제분석
    변수 : 전화번호(phone), 학번(id)
#알고리즘
    1. phone변수(딕셔너리) 생성
    2. 반복
        for i in range(5):
        id=학번 저장
        pnum=전화번호 저장

    3. 조건
        if id in phone: # 학번이 전화번호부에 있다면
            전화번호 출력
'''
phone=dict()
for i in range(5):
    id=int(input(str(i+1)+"번째 학생 학번 입력 : "))
    pnum=int(input(str(i+1)+"번째 학생 전화번호 입력 : "))

    phone[id]=pnum # 학번, 전화번호 -> 전화번호부에 입력
print("학생 전화번호부가 완성되었습니다.")

id=int(input("검색을 원하는 학생의 학번 입력 : "))

if id in phone:
    print("입력학 학생의 전화번호 : ", phone[id])

else : 
    print("입력한 학생의 전화번호가 없습니다.")
