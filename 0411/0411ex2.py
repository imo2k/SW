'''
고욱현
2023.04.11
선택문 if-elif-else
성적이 90이상이면 'A', 80이상 90 미만이면 'B'
70이상 80미만이면 'C', 70미만이면 'F'
'''

score = int(input("점수 입력 : "))

if score >= 90: # 조건 1
    print("A") # 조건 1이 참인 경우

elif score >= 80: # 조건 2
    print("B") # 조건 2가 참인 경우

elif score >= 70: # 조건 3
    print("C") # 조건 3이 참인 경우

else : 
    print("F") # 조건 1, 2, 3이 거짓인 경우

print("수고하셨습니다.")