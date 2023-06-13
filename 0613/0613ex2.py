'''
2023.06.13
고욱현

#문제정의
    하나의 숫자를 입력 받아서 1~ 입력받은 숫자 사이의
    약수를 구하는 dnumber()함수 구현하기
#알고리즘
    1. dnumber()함수 선언
        1-1. 약수 구하기
    2. 정수 입력 받기
    3. 약수를 저장할 리스트 변수 선언
    4. dnumber()함수 호출
    5. 약수 리스트 출력
'''
def dnumber(num, num_list): # dnumber()함수 선언
    
    # 약수 구하기
    for i in range(1, num+1): 
        if num % i ==0:
            num_list.append(i)

num = int(input("자연수를 입력하세요 : ")) # 정수 입력 받기
num_list=[] # 약수를 저장할 리스트 변수 선언

if num > 0:
    dnumber(num, num_list) #dnumber()함수 호출
    print(num, "의 약수는 : ", num_list)

else : 
    print(num, "은 자연수가 아닙니다.")