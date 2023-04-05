'''
2023.04.05
고욱현
P.116 9번 문제풀이(월급과 수당을 입력받아 세금을 뺀 실지급 될 월급 수령액을 계산하기)
'''
# Step 1. 변수 선언
salary = int(input("본봉(단위:만원) : "))
insen = int(input("수당(단위:만원) : "))

# Step2. 세금 계산
tax = (salary + insen) * 0.2

# Step3. 총액 계산
money = salary + insen - tax

# Step4. 결과 출력
print("본봉은 {}이고 수당이 {}일 때 실수령액은 {}이다".format(salary, insen, money))
print("이번달 월급 수령액은 {}만원입니다.".format(money))