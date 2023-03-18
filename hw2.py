def get_integer(prompt):
    m = int(input(prompt))
    return m

def exchange(n):
    n500 = n//500
    n %=500
    n100 = n//100
    n %=100
    n50 = n//50
    n %=50
    n10 = n//10
    print("500원 동전의 개수 : %d \n 100원 동전의 개수 : %d \n 50원 동전의 개수 : %d \n 10원 동전의 개수 : %d"%(n500,n100,n50,n10))

money = get_integer("동전으로 교환하고자 하는 금액은?")
exchange(money)
