# 먼저 들어간게 먼저 나와야함 선입선출 큐 이용
# 비슷한 아이디어로 시작했으나 이렇게 구현하지는 못함
# 큐 구현하는거 더 공부 필요
from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        now = q.popleft()
        sec = 0
        for i in q:
            sec += 1
            if now > i:
                break
        answer.append(sec)

    return answer