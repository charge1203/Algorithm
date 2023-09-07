import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())  # 간선 역할
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는거 0으로!
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # 틀린부분, 연결하는 노선은 하나가 아닐 수 있음!
    if c<graph[a][b]:  # 이 조건이 빠졌었음!!!!!
        graph[a][b] = c

# 플로이드워셜 알고리즘
for k in range(1,n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] >= INF:
            print(0, end=' ')  # 도달할 수 없는 경우 0 출력
        else:
            print(graph[a][b], end=' ')
    print()
