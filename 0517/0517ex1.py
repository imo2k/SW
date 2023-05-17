'''
2023.05.17
고욱현
for문을 이용한 파일 읽기
'''
#for 반복문으로 파일 읽어오기

with open("/Users/o2k/data/linetest.txt", "r") as f: # 파일 열기
    for line in f: # 파일 객체를 지정해서 반복문 작성
        print(line, end='') #줄 바꿈 없이 출력

#readline(): (한 줄씩 읽어오기) 메소드로 파일 읽어 오기)

print()

with open("/Users/o2k/data/linetest.txt", "r") as f:#파일 열기
    while True: # 무한 반복
        line=f.readline() #파일 한 줄 읽어오기
        print(line,end='') #줄 바꿈 없이 출력

        if line=='': # 읽어 올 내용이 없다면
            break # 반복 종료

#readlines(): 한 줄 씩 읽어서 리스트형으로 반환
print()

with open("/Users/o2k/data/linetest.txt", "r") as f: #파일 열기
    textlists=f.readlines() # 한 줄씩 리스트 형식으로 읽어오기
    print(type(textlists)) # 변수 타입 확인
    print(textlists) # 리스트 출력


#print() 함수로 파일에 출력하기
f=open("/Users/o2k/data/ptest.txt", "w") #쓰기 모드의 파일 객체 생성

print("aaaaaaa", file=f) # 파일에 출력
print("bbbbbbb", file=f) # 파일에 출력
print("ccccccc", file=f) # 파일에 출력

f.close()