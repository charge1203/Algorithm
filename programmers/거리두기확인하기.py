from collections import deque

def bfs(p):
    start = []
    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:  # 모든 인간이 있는 점에 대해~
        queue = deque([s])  # 큐에 초기값
        visited = [[0] * 5 for i in range(5)]  # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):  # 상하좌우 탐색
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:  # 범위 내 + 방문 안한 곳에 대해

                    if p[ny][nx] == 'O':  # 책상이면
                        queue.append([ny, nx])  # 일단 책상 좌표 큐에 넣고
                        visited[ny][nx] = 1  # 방문처리하고
                        distance[ny][nx] = distance[y][x] + 1  # 거리업뎃

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:  # 하지만 사람 발견
                        return 0  # 거리두기 실패
    return 1  # 모든 사람에 대해 다 훑었는데도 실패가 없다면 성공

def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    return answer