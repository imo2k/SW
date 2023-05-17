'''
2023.05.17
고욱현
#문제정의
    기존파일을 새로운 파일에 복사하는 프로그램 만들기
#문제분석
    변수 : 원본파일 입력(source), 복사 할 파일(target)
            , 원본 파일의 내용(texts)
#알고리즘
    1. source에 원본 파일 이름 입력
    2. target에 복사 할 파일 이름 입력
    3. 파일 처리
        source파일 객체 생성
            한 줄씩 읽어오기
            내용을 texts변수에 저장
        target파일 객체 생성
            texts파일 쓰기
        파일 생성 메시지 출력
'''
source=input("source 파일 입력 : ")  #source파일 객체 생성
target=input("target 파일 입력 : ")  #target파일 객체 생성

with open("/Users/o2k/data/linetest.txt", "r") as f: #읽기 파일 객체
    texts=f.read() # 파일 한꺼번에 문자열로 읽기

with open("/Users/o2k/data/copylinetest.txt", "w") as fp: #쓰기 파일 객체
    fp.write(texts)

    print(target+" 파일이 생성되었습니다. ") #메시지 출력

