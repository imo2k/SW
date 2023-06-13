'''
2023.06.13
고욱현

#문제정의
    3개의 매개변수를 전달 받아서 가장 큰 값을 리턴하는 
    findmax(a,b,c)함수 구현
#알고리즘
    1. findmax함수 선언
        1-1. a,b,c 중  가장 큰 값 찾기
    2. num1, num2, num3 값 입력 받기
    3. findmax(num1, num2, num3) 호출
    4. return문으로 반환되는 값 중 가장 큰 값 출력
'''
def findmax(a,b,c): #findmax 함수 선언
    
    # 가장 큰 값 찾기
    if a>b:
        biggest = a
    else:
        biggest = b

    if biggest < c:
        biggest = c

    return biggest

# num1, num2, num3 입력 받기
num1 = int(input("첫 번쨰 숫자 입력 : "))
num2 = int(input("두 번쨰 숫자 입력 : "))
num3 = int(input("세 번쨰 숫자 입력 : "))

# findmax(a,b,c) 호출
biggest_number = findmax(num1, num2, num3)

# return문으로 반환되는 값 중 가장 큰 값 출력
print("가장 큰 수는 : ", biggest_number)
