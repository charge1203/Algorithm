# 실버3
# deque rotate 처음 사용해봄
# 함수 안에 음수를 넣게 된다면 왼쪽 회전 양수는 오른쪽 회전
# 다시 풀어보기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
q = deque(enumerate(map(int, input().rstrip().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))