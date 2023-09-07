# 위상정렬
# 인접한 노드 확인할 때, 인접한 노드에 대하여 현재보다 강의시간이 더 긴 경우 찾는다면
# 더 오랜 시간이 걸리는 경우의 시간 값을 저장하는 방식으로 결과 테이블 갱신

import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)  # 각 강의 시간 0으로 초기화

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 첫번째는 시간 정보
    for x in data[1:-1]:  # x는 인접한 노드 번호 (선수과목 노드 번호)
        indegree[i] += 1  # x 개수만큼 indegree
        graph[x].append(i)  # x->i

def topology_sort():
    result = copy.deepcopy(time)  # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])

topology_sort()