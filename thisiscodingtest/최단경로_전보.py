# 다익스트라
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int, input().split())
graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
distance = [INF] * (n+1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (거리, 노드)
        if distance[now] < dist: # 현재 노드가 이미 처리된 적 있는 노드라면
            continue  # 무시
        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드 확인
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

count = 0  # 도달할 수 있는 노드 수
max_distance = 0  # 도달할 수 있는 노드 중, 가장 멀리 있는 노드와 최단거리

for d in distance:  # 모든 저장된 노드별 거리에서
    if d != INF:  # 도달할 수 있는 노드라면
        count += 1
        max_distance = max(max_distance, d)

# 시작노드는 제외해야하므로, count-1
print(count-1, max_distance)