# 구현
# 실버3
# 한 번에 못품 다시 풀자...

import sys
from collections import deque

c = int(input())
for _ in range(c):
    # m은 원하고자 하는 것의 현재 위치
    n, m = map(int, sys.stdin.readline().rstrip().split())
    q = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    idx = deque(range(n))
    count = 0

    while q:
        if q[0] == max(q):  # 첫번째가 가장 크다면
            count += 1
            q.popleft()
            pop_idx = idx.popleft()
            if pop_idx == m:
                print(count)

        else:
            q.append(q.popleft())
            idx.append(idx.popleft())
