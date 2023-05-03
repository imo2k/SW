'''
2023.05.03
고욱현
1~10까지 합계 구하기
'''

#while반복
i=1 #반복 횟수 초기화
sum=0 #합계
while i <= 100 : #반복 조건
    sum=sum+i #합계 저장
    i=i+1 # i 1증가
print('1부터 100까지의 합계 : ', sum)


#for반복
total=0 #합계
for i in range(1,11): #반복조건
    total = total + i #합계 구하기
print('1부터 10까지의 합계 : ', total)