from collections import deque

visited = [[False] * n for _ in range(n)]
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상,하,좌,우
graph = [[] * n for _ in range(n)]

for i in range(n):
    color = str(input())  # 색 입력 받기
for x in color:
    graph[i].append(x)


def bfs(x, y, color):
    q = deque()  # 큐 구현 위해 deque 라이브러리 이용


q.append([x, y])

while q:  # 큐가 빌 때까지 반복
    loc = q.popleft()
    x = loc[0]
    y = loc[1]

    if visited[x][y] == False:  # 비어있을 때
        visited[x][y] = True  # 방문
        for i in range(4):  # 네 방향 확인
            nx, ny = x + move[i][0], y + move[i][1]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:  # 영역 내
                if graph[nx][ny] == color:
                    q.append([nx, ny])

# 색약 아닐 때
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:  # 방문하지 않은 곳
            color = graph[i][j]
    bfs(i, j, color)
    cnt += 1

# 색약일 때
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':  # 초록색을
            graph[i][j] = 'R'  # 빨간색으로 취급

cnt_color_weakness = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = graph[i][j]
    bfs(i, j, color)
    cnt_color_weakness += 1

print(cnt)
print(cnt_color_weakness)
