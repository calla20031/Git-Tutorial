def read_single_dight(n):
    if n =='1' :
        return "일"
    elif n =='2' :
        return "이"
    elif n =='3' :
        return "삼"
    elif n =='4' :
        return "사"
    elif n =='5' :
        return "오"
    elif n =='6' :
        return "육"
    elif n =='7' :
        return "칠"
    elif n =='8' :
        return "팔"
    elif n =='9' :
        return "구"
    elif n =='0' :
        return "영"

num = int(input("세 자리 정수 입력 : "))
def read_number(num):
    num1 = str(num)
    f = num1[0]
    s = num1[1]
    t = num1[2]
    fr = read_single_dight(f)
    se = read_single_dight(s)
    th = read_single_dight(t)
    return fr, se, th
result = read_number(num)
frist = result[0]
second = result[1]
thrid = result[2]
print(frist, second, thrid)
