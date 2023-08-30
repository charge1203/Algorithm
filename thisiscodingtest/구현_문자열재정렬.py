# 기존 리스트에 하니까 리스트 순환할 때 삭제하면 누락 발생
# 새로운 리스트 선언하여 그냥 append

import sys
s = sys.stdin.readline().rstrip()
answer = []
integer = 0

for i in s:
    if i.isdigit():
        integer += int(i)
    else:  # i.isalpha()
        answer.append(i)

answer.sort()
if integer != 0:  # 이거 주의!!!!!!!!!
    answer.append(str(integer))
print(''.join(answer))