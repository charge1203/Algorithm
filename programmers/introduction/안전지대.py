# 맞췄다 기분 좋다
# BFS를 애매하게 씀?
def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    # 상하좌우 대각들
    dx = [0, 0, -1, 1, 1, -1, 1, -1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    safe = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:  # 지뢰 있으면
                safe[i][j] += 1
                for k in range(8):  # 상하좌우대각서치
                    nx = i + dx[k]
                    ny = j + dy[k]

                    # 공간 넘어간 경우
                    if nx < 0 or nx >= col or ny < 0 or ny >= row:
                        continue
                    if board[nx][ny] != 0:  # 지뢰있으면 넘어가기
                        continue
                    else:
                        safe[nx][ny] += 1

    for i in safe:
        answer += i.count(0)
    return answer


# BFS 쓴 풀이
from collections import deque

def solution(board):
    dx = [-1, 1, 0 , 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    length = len(board)
    visited = [[False] * length for _ in range(length)]

    def bfs(x, y):
        dq = deque()
        dq.append((x, y))
        while dq:
            a, b = dq.popleft()
            visited[a][b] = True
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                #위험지역으로 둬야함
                if 0<=nx<length and 0<=ny<length and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        dq.append((nx, ny))
                    else:
                        board[nx][ny] = 2 #위험지역 처리

    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bfs(i, j)
    result = 0
    for i in range(length):
        result += board[i].count(0)
    return result