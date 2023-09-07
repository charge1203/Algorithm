# 간단한 다익스트라 알고리즘
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 순차탐색

import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

n,m = map(int, input().split())  # 노드 개수, 간선 개수 입력받기
start = int(input())  # 시작 노드 입력 받기
graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
visited = [False] * (n+1)  # 방문한 적이 있는지 체크하는 목적의 리스트
distance = [INF] * (n+1)  # 최단 거리 테이블을 모두 무한으로 초기화

# 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())  # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드의 인덱스 저장할 곳
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0  # 시작 노드 초기화
    visited[start] = True  # 시작 노드 초기화
    for j in graph[start]:
        distance[j[0]] = j[1]  # j[0] 노드까지의 거리는 j[1] (b,c)

    for i in range(n-1):  # 시작 노드 제외한 전체 n-1개의 노드 대해 반복
        now = get_smallest_node()  # 현재 최단 거리가 가장 짧은 노드 반환
        visited[now] = True  # 현재 최단 거리가 가장 짧은 노드 방문 처리

        for j in graph[now]:  # 현재 노드와 연결된 다른 노드 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:  # 현재 노드 (now)를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost

dijkstra(start)  # 다익스트라 알고리즘 수행

# 모든 노드로 가기 위한 최단 거리
for i in range(n+1):
    if distance[i] == INF:  # 도달할 수 없는 경우
        print('INFINITY')
    else:
        print(distance[i])


# 개선된 다익스트라 알고리즘 코드
# 최단 거리가 가장 짧은 노드를 선택하는 과정은 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

n,m = map(int, input().split())  # 노드 개수, 간선 개수 입력받기
start = int(input())  # 시작 노드 입력 받기
graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
distance = [INF] * (n+1)  # 최단 거리 테이블을 모두 무한으로 초기화

# 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())  # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra2(start):
    q = []
    heapq.heappush(q,(0,start))  # 시작 노드로가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (거리, 노드)
        if distance[now] < dist:  # 현재 노드가 이미 처리된 적 있는 노드라면
            continue  # 무시
        for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드 확인
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra2(start) # 알고리즘 수행

# 모든 노드로 가기 위한 최단 거리
for i in range(n+1):
    if distance[i] == INF:  # 도달할 수 없는 경우
        print('INFINITY')
    else:
        print(distance[i])
