# 얼음 얼리는 공간을 그래프 형태로 모델링
# '0'인 값이 상,하,좌,우로 연결되어 있는 노드를 묶는 프로그램을 작성

import sys
# sys.setrecursionlimit(10**6)
n,m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False #주어진 범위를 벗어나는 경우에는 즉시 종료
    if graph[x][y] == 0: #현재 노드를 방문하지 않았다면
        graph[x][y] == 1 #해당 노드 방문 처리
        #상,하,좌,우의 위치도 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: #현재 위치에서 DFS 수행
            result += 1

print(result)

