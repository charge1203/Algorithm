# 골드5
# 정렬
# 우선순위 큐 이용

# sol1
# 런타임에러??
import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
schedules = sorted([list(map(int, input().rstrip().split())) for _ in range(n)])
h = []

for start,end in schedules:
    if h and h[0] <= start:
        heapq.heappush(h)
    heapq.heappush(h, end)

print(len(h))


# sol2
import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
schedules = []

for _ in range(n):
    schedules.append(list(map(int, input().rstrip().split())))

schedules.sort(key = lambda x: x[0])
cnt = 1

b = [0]

for start,end in schedules:
    if start >= b[0]:
        heapq.heappop(b)
    else:
        cnt+=1
    heapq.heappush(b, end)

print(cnt)