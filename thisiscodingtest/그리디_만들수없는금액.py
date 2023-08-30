# 다시 풀어야하는 문제

import sys

n = int(sys.stdin.readline())
coin = list(map(int, sys.stdin.readline().split()))
coin.sort()

min = 1

for i in coin:
    if min < i:
        break
    min += i  # 이거를 못함.... 거의 다 했었네...
print(min)