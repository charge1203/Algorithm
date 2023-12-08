# max_heap 구조로 만들어서 n번째 값 뽑으면 되는거 아니야?
# max_heap 구조는 - 붙여서 heapq에 넣는거

try1 -> 메모리 초과
import sys, heapq
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    num_list = list(map(int, input().split()))
    for j in num_list:
        heapq.heappush(q, -j)
print(-q[n-1])


# try2
# 공간복잡도 고려, q의 크기가 너무 커지지 않게
import sys, heapq
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    num_list = list(map(int, input().split()))
    if not q:
        for j in num_list:
            heapq.heappush(q, j)
    else:
        for num in num_list:
            if q[0] < num:  # q에 들어있는 최솟값보다 num(현재숫자)이 클 때
                heapq.heappop(q)  # q의 최솟값 제거
                heapq.heappush(q, num)  # 큰 건 넣어
print(heapq.heappop(q))
