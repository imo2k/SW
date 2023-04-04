'''
2023.04.04
고욱현
표준출력 (print) format() 연습
'''

print('이름은 {}이고 나이는 {}세 입니다.'.format('고욱현', 25)) #순서대로 mapping

print('이름 {name}, 나이 {age}, 주소 {add}'.format(add='Busan', name='고욱현', age='25'))
# 변수로 지정했기 때문에 순서 상관 x
print('The lucky number is ({:14})'.format(7777777)) # 숫자는 기본적으로 오른쪽 정렬

print('The lucky is ({:<14})'.format(7777777)) # 숫자 왼쪽 정렬

