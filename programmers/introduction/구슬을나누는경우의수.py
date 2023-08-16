import math

def solution(balls, share):
    answer = math.factorial(balls)/(math.factorial(balls-share)*math.factorial(share))
    return answer

# 다른 풀이

# factorial 코드가 기니까
from math import factorial as fac

def solution1(balls, share):
    answer = fac(balls)/(fac(balls-share)*fac(share))
    return answer

# math.comb 사용

def solution2(balls, share):
    return math.comb(balls, share)

# 직접 factorial 함수 정의
def fac(num):
    a = 1
    for i in range(1, num+1):
        a *= i
    return a