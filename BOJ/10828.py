# 구현
# 브론즈1
# push는 출력이 아님

import sys

n = int(sys.stdin.readline().rstrip())
command = []
stack = []

for _ in range(n):
    command.append(sys.stdin.readline().rstrip())

for i in command:
    if i.startswith('push'):
        integer = i.split()[1]
        stack.append(integer)
    if i == 'top':
        print(-1 if not stack else stack[-1])
    elif i == 'size':
        print(len(stack))
    elif i == 'empty':
        print(1 if not stack else 0)
    elif i == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

