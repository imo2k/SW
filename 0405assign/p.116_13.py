'''
고욱현
P.116 13번
'''

# 변수 선언하기
food = int(input("음식 요금(단위:원) : "))

# 부가세 계산하기
vat = food * 1.1

# 총 식사 비용 계산하기
pay = food + vat

# 결과 출력하기
print("음식 요금은 {}이고 지불 하실 식사 금액은 {}원 입니다".format(food, pay))


