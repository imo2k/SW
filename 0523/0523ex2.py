'''
2023.05.23
고욱현
#문제정의
    키보드로 입력받은 내용을 리스트에 저장하고 파일(out.txt)에 출력하기
#문제분석
    변수 : 입력값을 저장할 리스트(enter), 키보드 입력 내용 저장(txt)

#알고리즘
    1. 변수 초기화
        enter = []
    2. 파일열기 객체 생성(쓰기)
    3. 파일 처리
        3-1. (반복) While True:
                        texts=문장입력
                        (선택) if texts=='':
                                    break
                        text를 enter(리스트 변수) 추가
        3-2. 파일게 결과 출력
    4. 파일 닫기
'''
enter=[] #리스트 변수

f=open("/Users/o2k/data/out.txt", "w") # 파일 쓰기 객체

while True:
    texts=input("문장 입력 (종료 : 엔터키) : ") #문자열 입력
    if texts=='': # 공백인 경우 반복 종료
        break
    enter.append(texts+"\n") #입력한 내용 리스트에 추가

print("입력될 리스트 : ", enter)

f.writelines(enter)# 리스트 자료형을 파일에 출력
f.close()

print("out.txt 파일이 생성되었습니다.")
