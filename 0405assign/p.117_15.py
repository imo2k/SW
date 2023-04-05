'''
고욱현
P.117 15번
'''
# 변수 선언
ctax = int(input("자동차 세금 :"))

#가산금 계산하기
ptax = ctax * 0.03

#최종 자동차 세금 계산하기
ftax = ctax + ptax

#결과 출력하기
print("자동차 세금은 {}원이고 가산금은 {}원이므로 최종 자동차 세금은 {}원입니다.".format(ctax, ptax, ftax))