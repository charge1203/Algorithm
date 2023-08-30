# 완전탐색

import sys

n = int(sys.stdin.readline())

h, m, s = 0, 0, 0
count = 0

for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
            # if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)