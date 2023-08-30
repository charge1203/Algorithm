# 구현

import sys

n = int(sys.stdin.readline())
num_list = []
result = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))

for i in num_list:
    if i != 0:
        result.append(i)
    else:
        result.pop()

print(sum(result))
