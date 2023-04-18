'''
2023.04.18
고욱현
3장 연습문제 7번
두 정수 입력 x>y-x//y, x<y->x+y, x==y->x*y
단 나눗셈 몫 계산할 때 y는 0 안됨
#문제분석
    변수 : 정수(num1), 정수(num2) 연산자op(>, <, ==)
    수식 : num1 (>, <, ==) num2
        
#알고리즘 
    1. 변수 선언
        num1 num2 op
    2. 논리(선택-중첩if문)
'''

x=int(input("x의 값을 입력해주세요 :"))
y=int(input("y의 값을 입력해주세요 :"))

if y == 0:
    print("y의 값이 0입니다.")
else:
    if x > y:
        print("{} // {} = {}".format(x, y, x//y))
    elif x < y:
        print("{} + {} = {}".format(x, y, x+y))
    else:
        print("{} * {} = {}".format(x, y, x*y))
