import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

# 이동할 네 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:  # 큐가 빌 때까지 반복
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간 넘어간 경우 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 벽? 괴물?인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드 처음 방문한 경우만 최단거리에 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]  # 가장 오른쪽 아래 최대한 거리 반환

print(bfs(0,0))