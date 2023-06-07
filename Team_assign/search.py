# 파일에서 데이터를 읽어와서 상품 이름으로 검색하는 부분
def search_product(product_name):
    found = False
    with open("products.txt", "r") as file:
        for line in file:
            # 각 줄을 쉼표로 분리하여 상품, 수량, 소비기한을 추출
            parts = line.strip().split(",")
            product = parts[0]
            quantity = parts[1]
            expiration = parts[2]

            # 상품 이름이 일치하는 경우 데이터를 출력
            if product.strip() == product_name.strip():
                print(f"상품: {product}")
                print(f"수량: {quantity}")
                print(f"소비기한: {expiration}")
                found = True
                break

    if not found:
        print("상품을 찾을 수 없습니다.")

# 사용자로부터 검색할 상품 이름 입력 받기
product_name = input("검색할 상품 이름을 입력하세요: ")

# 상품 검색
search_product(product_name)


