# 브루드포스 실버4

import sys
n = int(sys.stdin.readline().rstrip())
count = 0

for i in range(1,n+1):
    if len(str(i))==1 or len(str(i))==2:
        count += 1
    elif len(str(i))==3:
        if (int(str(i)[0])-int(str(i)[1])) == (int(str(i)[1])-int(str(i)[2])):
            count += 1

print(count)