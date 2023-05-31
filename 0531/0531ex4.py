'''
2023.05.31
고욱현

#문제정의
    튜플안에 있는 숫자들의 종류와 반복 갯수 분석하기
#문제분석

#알고리즘

'''

num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0) # 튜플
num_list=[] #빈리스트

for i in range(len(num)): #튜플 길이만큼 반복
    if num[i] not in num_list: #리스트에 없는 경우만 출력
        print(num[i], "개수 : ", num.count(num[i])) # 개수 출력
        num_list.append(num[i]) #리스트에 추가

''' 
# if 출력 결과 오름차순
num_list.sort()  # 리스트를 오름차순으로 정렬

for i in num_list:
    print(i, "개수:", num.count(i))  # 오름차순으로 정렬된 리스트에서 개수 출력'''