# 구현

import sys

e, f, c = map(int, sys.stdin.readline().split())

answer = 0
bottle = e+f  # 처음 가지고 있는 빈병

while bottle >= c:
    answer = answer + bottle//c
    bottle = bottle - (bottle//c)*c + (bottle//c)

print(answer)