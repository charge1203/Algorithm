# first try
# 다익스트라
# 맞음!!

import heapq
def solution(n, edge):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    q = []

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    heapq.heappush(q, (0, 1))  # 시작 노드로가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    distance[1] = 0
    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 현재 노드가 이미 처리된 적 있는 노드라면
            continue  # 무시
        for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드 확인
            cost = dist + 1
            if cost < distance[i]:  # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    return distance.count(max(distance[1:]))


# 다른 풀이
# BFS로 풀어보기
from collections import deque

def solution2(n, edge):
    answer = 0
    # 연결된 노드 정보 그래프
    graph = [[] for _ in range(n + 1)]
    # 각 노드의 최단거리 리스트
    distance = [-1] * (n + 1)

    # 연결된 노드 정보 추가
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([1])  # BFS를 위한 queue, 출발 노드 = 1
    distance[1] = 0  # 출발노드의 최단거리를 0으로

    # BFS 수행
    while queue:
        now = queue.popleft()  # 현재 노드

        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[now]:
            if distance[i] == -1:  # 아직 방문하지 않은 노드면,
                queue.append(i)  # queue에 추가
                distance[i] = distance[now] + 1  # 최단거리 갱신
    # 가장 멀리 떨어진 노드 개수 구하기
    for d in distance:
        if d == max(distance):
            answer += 1
    return answer