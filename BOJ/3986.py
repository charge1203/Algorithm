# 자료구조
# 실버4
# 처음에 문제 이해가 어려웠음
# 순차탐색으로 큐에 넣고 내가 지금 탐색하는 거랑 큐의 맨 위 원소가 같다면 둘다 빼고 ans 1 증가

import sys
n = int(sys.stdin.readline().rstrip())
count = 0

for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    stack = []

    for i in range(len(word)):
        if stack:
            if word[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(word[i])
        else:
            stack.append(word[i])

    if not stack:
        count += 1

print(count)