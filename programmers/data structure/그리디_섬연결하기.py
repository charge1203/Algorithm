# 크루스칼
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    edges = []
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    for i in costs:
        a, b, cost = i[0], i[1], i[2]
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
            union_parent(parent, edge[1], edge[2])  # 이걸 빼먹었었네
            answer += edge[0]

    return answer