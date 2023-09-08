# 크루스칼
# first try -> 메모리 부족
# 모든 간선을 구성해서 그럼
# 모든 간선을 만들어보지 않고, 선택될 가능성이 있는 간선만 구성해야함 -> 이 부분에서 어려웠음

# second try
import sys
input = sys.stdin.readline

n = int(input())
result = 0
edges = []
parent = [0] * (n+1)

# 좌표를 x,y,z 별로 저장하고 정렬
x,y,z = [],[],[]

for i in range(n):
    p,q,r = map(int,input().split())
    x.append((p,i))
    y.append((q,i))
    z.append((r,i))
x.sort(); y.sort(); z.sort()

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1,n+1):
    parent[i] = i

# 인접한 노드들부터 처리
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

print(edges)

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)


# first try
import sys
input = sys.stdin.readline

n = int(input())
result = 0
planet = []*(n+1)
edges = []
parent = [-1] * (n+1)

# 행성 번호 0~(n-1)
for _ in range(n):
    planet.append(list(map(int, input().split())))

def min_cost(a,b):
    return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(len(planet)):
    for j in range(i+1,len(planet)):
        edges.append((min_cost(planet[i], planet[j]), i, j))

for i in range(1,n+1):
    parent[i] = i

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)