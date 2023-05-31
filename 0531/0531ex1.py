'''
2023.05.31
고욱현

#문제정의
    10개의 난수를 발생시키고 리스트에 저장한 후 최대, 최소, 합계 구하기
#문제분석
    변수 : 빈 리스트(num)
#알고리즘
    1. 랜덤 모듈 추가
    2. 변수 초기화
        num = []
    3. 반복
        for i in range(10):
            난수 생성
            리스트에 추가
    4. 결과 출력(최대, 최소, 합계, 정렬)
'''
import random #난수

num = [] #난수 저장을 위한 리스트 변수

for i in range(10): # 반복 조건
    num.append(random.randint(1,100)) # 난수 방생 후 리스트 추가

print("생성된 리스트 : ", num)
print("가장 큰 값 : ", max(num))
print("가장 작은 값 : ", min(num))
print("전체 요소의 합 : ", sum(num))
num.sort() # 오름차순 정렬
print("정렬된 리스트 : ", num)
num.reverse() # 내림차순 정렬 (num.sort(reverse=True)도 가능)
print("정렬된 리스트 : ", num)