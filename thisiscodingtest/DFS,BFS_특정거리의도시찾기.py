import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * n

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)  # 모든 도시에 대한 최단 거리 초기화
distance[x] = 0  # 출발 도시까지의 거리는 0

# BFS
q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:  # now 노드에서 이동할 수 있는 모든 노드 확인
        if distance[i] == -1:  # 아직 방문하지 않음
            distance[i] = distance[now] + 1
            q.append(i)

# 최단거리가 k인 모든 도시 번호 오름차순 출력
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check=True

if check == False:
    print(-1)