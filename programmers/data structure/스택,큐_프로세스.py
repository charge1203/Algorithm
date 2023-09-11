# 젤 밑에  풀이가 젤 좋음

# first try
# 20점...
def solution(priorities, location):
    loc = priorities.index(max(priorities))

    for i in range(len(priorities)):
        if loc >= len(priorities):
            loc %= len(priorities)
        if loc == location:
            return i + 1
        loc += 1


# 큐 이용한 풀이 참고
# location을 줄여나가야 패턴이 맞는다는거.. 이해가 안되네
from collections import deque

def solution2(priorities, location):
    answer = 1  # 순서는 1부터 시작!
    q = deque(priorities)
    while len(q) > 1:
        tmp = q.popleft()
        if tmp < max(q):
            q.append(tmp)  # 다시 넣기
            if location == 0:
                location = len(q) - 1
            else:
                location -= 1
        else:
            if location == 0:
                return answer
            else:
                answer += 1
                location -= 1

    return answer

# 다른풀이
# stack??
def solution3(priorities, location):
    stack = [(i,p) for i,p in enumerate(priorities)]  # 인덱스와 prioirities 튜플에 저장
    answer = 0
    while True:
        tmp = stack.pop(0)
        if any(tmp[1] < q[1] for q in stack):  # 자기보다 큰게 있으면
            stack.append(tmp)  # 스택에 다시 넣기
        else:
            answer += 1
            if tmp[0] == location:
                return answer