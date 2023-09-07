# 크루스칼
# 2개의 최소 비용 신장 트리를 만들어야함
# 크루스칼 알고리즘 통해 최소 비용 신장 트리 만든 후 최소 신장 트리를 구성하는 간선 중 가장 비용이 큰 간선 제거

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
result = 0
parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort()
last = 0  # 최소비용신장트리에 포함된 간선 중에서 가장 비용이 큰 간선
# 비용이 작은거에서 큰 순서로 들어오니까 마지막에 들어온 간선 비용이 가장 큰거임

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result-last)
