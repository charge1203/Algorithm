# 모범답안이랑은 접근이 다르지만 나쁘지 않은듯?

import sys

s = sys.stdin.readline().rstrip()
count = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count+=1

if count%2 == 0:
    result = count/2
else:
    result = int(count/2)+1

print(int(result))


# 다른풀이
# 나랑 비슷한데 좀 더 간결

s = input()
cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1

print((cnt+1)//2)
