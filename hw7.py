shopping_bag = {}
while True:
    print("[구입]")
    item = input("상품명? ")
    if item != " ":
        num =int(input("수량은? "))
        shopping_bag[item] = num
    else:
        break
print(f">>> 장바구니 보기 : ", shopping_bag)
print("[검색]")
find = input("장바구니에서 확인하고자 하는 상품은 ? ")
if find in shopping_bag:
    find_num = shopping_bag[find]
    print(f"{find}은(는) {find_num}개 담겨 있습니다." )
