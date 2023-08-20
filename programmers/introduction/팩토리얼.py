import math
def solution(n):
    answer=0
    for i in range(1,11):
        if math.factorial(i) > n:
            answer = i-1
            break
        elif math.factorial(i) == n:
            answer=i
            break
    return answer

# 다른풀이
from math import factorial
def solution2(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

# 다른풀이
import math
def solution3(n):
    for i in range(1,12):
        if n < math.factorial(i):
            return i-1