import sys

n, m = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))

count = 0

for i in range(len(k)):
    for j in range(i+1, len(k)):
        if k[i] != k[j]:
            count += 1

print(count)
