# 그리 맘에 들지 않음.. 꾸역꾸역...
def solution(a, b):
    d = 2
    lst = []
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            a = a / i
            b = b / i
    while d <= b:
        if b % d == 0:
            lst.append(d)
            b = b // d
        else:
            d += 1

    new_list = [i for i in lst if i != 2 and i != 5]

    if not new_list:
        return 1
    else:
        return 2


# 다른풀이
# gcd 이용하기!!!!
from math import gcd
def solution2(a, b):
    b //= gcd(a,b)  # 최대공약수로 나누면 기약분수 되니까. 그리고 분모만 필요함
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2