def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area():
    s = 3.14*r*r
    return s
r = get_radius("넓이를 구하고자 하는 원의 반지름은?")
s = get_circle_area()
print("반지름",r,"인 원의 넓이 = 3.14 x",r,"x",r,"=",s)
