'''
2023.04.05
고욱현
P.117 14번 문제풀이(5과목의 점수 총점과 평균구하기)
'''
# Step 1. 변수 선언
sub1 = int(input('과목1 : '))
sub2 = int(input('과목2 : '))
sub3 = int(input('과목3 : '))
sub4 = int(input('과목4 : '))
sub5 = int(input('과목5 : '))

# Step 2. 총헙
total = sub1 + sub2 + sub3 + sub4 + sub5

# Step 3. 평균
avg = total / 5

# Step 4. 출력
print("5과목의 합계는 {}이고, 평균은 {}이다.".format(total, avg))