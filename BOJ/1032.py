# 구현
# 브론즈1

import sys

n = int(sys.stdin.readline().rstrip())
name = []

for _ in range(n):
    name.append(sys.stdin.readline().rstrip())

pattern = [''] * len(name[0])

for i in range(n):
    for j in range(len(name[i])):
        if pattern[j] == '':
            pattern[j] = name[i][j]  # 이렇게 안하고 pattern을 name[0]의 리스트로 저장했어도 됨
        if pattern[j] != name[i][j]:
            pattern[j] = '?'

print(''.join(pattern))

