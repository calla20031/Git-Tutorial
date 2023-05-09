shopping_bag = {}

def buy():
    while True:
        item = input("상품명? ")
        if item !=" ":
            num = int(input("수량은? "))
            shopping_bag[item]=num
        else:
            break
def show(s):
    for n in s:
        print(n, end=" ")
    print()
def find(lst,n):
    if n not in lst:
        return None
    return shopping_bag[n]

print("[구입]")
items = buy()

print("\n>>>장바구니 보기", shopping_bag)


print("[검색]")
s = input("장바구니에서 확인하고자 하는 상품은? ")
idx = find(shopping_bag,s)
if idx != None:
    print(f"{s}점은 {idx}개 담겨 있습니다.")
else:
    print(f"장바구니에 {s}은(는) 없습니다.")
