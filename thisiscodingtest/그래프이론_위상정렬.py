import sys
from collections import deque
input = sys.stdin.readline

v,e = map(int, input().split())  # 노드 개수, 간선 개수 입력 받기
indegree = [0] * (v+1)  # 모든 노드에 대한 진입차수 0으로 초기화
graph = [[] for _ in range(v+1)]  # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화

# 간선 정보 입력 받기
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)  # 노드 a에서 노드 b로 이동
    indegree[b] += 1  # b로 간거니 b의 진입차수 1 증가

# 위상정렬 함수
def topology_sort():
    result = []  # 알고리즘 수행 결과 담을 리스트
    q = deque()

    # 처음 시작에 진입차수가 0인 노드 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:  # 큐가 빌 때까지 반복
        now = q.popleft()  # 현재 사용할 노드 큐에서 꺼내기
        result.append(now)
        for i in graph[now]:  # now 노드와 연결된 노드들의 진입차수 1씩 빼기
            indegree[i] -= 1
            if indegree[i] == 0:  # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()