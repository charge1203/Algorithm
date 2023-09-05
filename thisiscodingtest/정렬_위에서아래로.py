import sys
n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

num = sorted(num, reverse=True)

for i in num:
    print(i, end=' ')