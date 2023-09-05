# 이렇게 간단한 문제인데.. 못풀었음

import sys

n = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))
house.sort()

print(house[(n-1)//2])
