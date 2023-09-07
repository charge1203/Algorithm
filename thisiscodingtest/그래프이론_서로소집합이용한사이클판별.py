import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기, 경로 압축으로 find 함수 재귀적 호출하여 부모 테이블 값 갱신
def find_parent(parent, x):
    if parent[x] != x:  # 루트 노드가 아니라면
        parent[x] = find_parent(parent, parent[x])  # 루트 노드를 찾을 때까지 재귀적 호출
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)  # 부모 노드 반환
    b = find_parent(parent, b)  # 부모 노드 반환
    if a < b:
        parent[b] = a  # b가 더 크다면 b가 a를 가르킴
    else:
        parent[a] = b

v,e = map(int, input().split())  # 노드 개수, 간선 개수(=union 연산)
parent = [0] * (v+1)  # 부모테이블 만들기

for i in range(1,v+1):
    parent[i] = i  # 부모테이블에서 부모를 자기자신으로 초기화

cycle = False  # 사이클 발생 여부

# union 연산 수행
for i in range(e):
    a,b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):  # 부모노드가 같다면
        cycle = True  # 사이클이 발생한 것
        break  # 종료
    else:  # 부모노드가 달라 사이클이 발생하지 않았다면
        union_parent(parent, a,b)  # union 연산 수행

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')