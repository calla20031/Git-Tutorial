discount = int(input("할인율은?"))
a_price = int(input("A상품의 할인된 가격은?"))
b_price = int(input("B상품의 할인된 가격은?"))

def get_fixed_price(price,discount):
    before_price = price*100/(100-discount)
    return before_price

aprice = get_fixed_price(a_price, discount)
bprice = get_fixed_price(b_price, discount)

print("A 상품의 정가는 %d원"%aprice)
print("B 상품의 정가는 %d원"%bprice)

