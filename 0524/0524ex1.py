'''
2023/05/24
고욱현
#문제정의
    난수를 발생시켜 num.txt 파일을 만들고, 이 파일을 이용해서 각 학생의
    평균을 구한 후 avg.txt 파일에 저장하기
#문제분석

#알고리즘
'''

import random # 난수 모듈 추가
with open("/Users/o2k/data/num.txt", "w") as f: #파일 객체
    for i in range(5): #줄 반복
        for j in range(5): #랜덤 수 찍기 반복
            f.write(str(random.randint(1, 100))) #랜덤 수 파일에 쓰기
            f.write(' ') # 솟자 다음 공백 찍기
        f.write('\n') # 줄 바꿈

with open("/Users/o2k/data/num.txt", "r") as f1: # 읽기 파일 객체
    with open("/Users/o2k/data/avg.txt", "w") as f2: # 쓰기 파일 객체

        j=0
        while True: #무한 반복
            j += 1
            score=f1.readline() # num.txt 한 줄 읽어오기
            if score == '': # 내용 없으면 반복 중지
                break
            scorelist=score.split() # 읽어 온 한 줄을 공백 기준으로 리스트화
            
            sum=0 #합계

            for i in range(5): #한 학생당 5과목의 점수 더하기 반복
                sum += int(scorelist[i]) # scorelist의 항목 더하기

            print(j, "번 학생의 평균 점수 : ", sum/5, file=f2) # 결과 파일에 작성


