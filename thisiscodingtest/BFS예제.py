from collections import deque

def bfs(graph, start, visited): #BFS 메서드 정의
    queue = deque([start]) #큐 구현 위해 deque 라이브러리 사용
    visited[start] = True #현재 노드 방문 처리
    while queue: #큐가 빌 때까지 반복
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]: #인접하고 아직 방문하지 않은 원소들 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2,3,8], [1,7], [1,4,5],
         [3,5], [3,4], [7], [2,6,8], [1,7]]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)