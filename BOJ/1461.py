# 골드4
import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
book = list(map(int, sys.stdin.readline().rstrip().split()))

neg = []
pos = []
for item in book:
    if item < 0:
        neg.append(abs(item))
    elif item > 0:
        pos.append(item)

neg.sort(reverse=True)
pos.sort(reverse=True)

result = []

for i in range(len(pos)):
    if i%m == 0:
        result.append(pos[i])
for i in range(len(neg)):
    if i%m == 0:
        result.append(neg[i])

result.sort()
answer = 2*sum(result) - result[-1]
print(answer)