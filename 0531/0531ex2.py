'''
2023.05.31
고욱현
#문제정의
    2차원 리스트의 학생 점수를 참고하여
    각 학생의 3과목 총점 구하기
#문제분석
    변수 : 점수 리스트 (num), 합계(j)
#알고리즘
    1. 점수 리스트 선언
    2. 반복 조건
        for i in range(len(num[0])):
'''
num=[[20001, 20002, 20003, 20005, 20005] #학번
    ,[89,74,88,99,95] #점수1
    ,[91,75,68,98,88] #점수2
    ,[79,94,68,94,92]] #점수3

j=0

for i in range(len(num[0])): # 반복조건 (길이만큼 반복)
    print(num[j][i], "학생의 총점은 : ", num[j+1][i]+num[j+2][i]+num[j+3][i])