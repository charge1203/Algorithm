# 얜 풀 수 있어야함
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * (n + 1)
    # bfs
    # for i in range(n):
    #     if not visited:
    #         bfs(n,computers, i, visited)
    #         answer += 1

    # dfs
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1
    return answer


def bfs(n, computers, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for i in range(n):  # 이거떔에 틀렸엄
            if i != now and computers[now][i] == 1:  # 자기자신이 아닌 1로 연결되어있는 노드
                if not visited[i]:
                    q.append(i)
                    visited[i] = True


def dfs(n, computers, start, visited):
    visited[start] = True
    for i in range(n):
        if i != start and computers[start][i] == 1:  # 연결
            if not visited[i]:
                dfs(n, computers, i, visited)