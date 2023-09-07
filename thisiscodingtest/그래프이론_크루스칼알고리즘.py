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

n,e = map(int, input().split())  # 노드 개수와 간선 개수(=union연산) 입력받기
parent = [0] * (n+1)  # 부모테이블 생성

for i in range(1,n+1):  # 부모테이블 자기자신으로 초기화
    parent[i] = i

edges = []  # 모든 간선 정보 담을 리스
result = 0  # 최종 비용

for _ in range(e): # 간선 정보 입력 받기
    a,b,cost = map(int, input().split())
    # 비용순 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))

edges.sort()  # 간선을 비용순 정렬

for edge in edges:  # 간선 하나씩 확인
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):  # 사이클이 발생하지 않을때만
        union_parent(parent,a,b)  # 합집합 하고
        result += cost  # cost 더하기

print(result)
