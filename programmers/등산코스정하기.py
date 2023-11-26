import heapq
INF = int(1e9)

def solution(n, paths, gates, summits):
    # 간선 정리 (양방향)
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    # 산봉우리 판별
    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True

    # gates 모두 시작 위치
    distance = [INF] * (n + 1)
    q = []
    for gate in gates:
        distance[gate] = 0
        # 시작노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
        heapq.heappush(q, [0, gate])

    # 다익스트라
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 산봉우리면 바로 continue
        # 이렇게 해야 두 개 이상의 산봉우리를 방문하지 않는다.
        if distance[now] < dist or is_summit[now]:
            continue
        for j, cost in graph[now]:  # now위치에서 이어지는 j노드와 cost에 대해
            cost = max(distance[now], cost)
            if distance[j] > cost:
                distance[j] = cost
                heapq.heappush(q, [cost, j])

    # 결과
    # 거리가 같으면 산봉우리의 번호가 작은 것을 출력해야 하므로
    # 산봉우리를 정렬하여 살펴보자.
    result = [-1, INF]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    return result