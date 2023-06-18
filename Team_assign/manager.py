'''
팀프로젝트

#고욱현
#김대영
#김태환

#물류관리(재고조사) 프로그램

-물류가 들어오고 검수할 때 유통기한 및 수량을 파악하고 입출고 현황조회가 가능한 프로그램
-큰 틀로 1차로 종류 정리하기 (의류, 유제품류, 전자기기 등등)
-상품명, 유통기한, 수량 입력받기
-리스트 출력으로 조회
-출고 할 물품을 입력받기
-수량을 입력받아서 출고처리

'''
# 상품 데이터를 저장할 리스트
products = []

# 사용자 입력을 받아 상품, 수량, 소비기한을 저장하는 부분
product = input("상품 이름을 입력하세요: ")
price = input("상품의 가격을 입력해주세요:")
quantity = input("수량을 입력하세요: ")
expiration = input("소비기한을 입력하세요: ")

# 입력된 데이터를 리스트에 저장
products.append([product, price, quantity, expiration])

# 리스트를 파일에 저장하는 함수
def save_products():
    with open("products.txt", "w") as file:
        for product in products:
            file.write(",".join(product) + "\n")

# 상품 데이터를 파일에 저장
save_products()

