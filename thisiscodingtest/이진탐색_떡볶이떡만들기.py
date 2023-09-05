# 이진탐색으로 못품
# 하지만 전형적인 이진탐색 문제라고 함..
# 이 코드는 순차탐색으로 시간초과 받을 가능성 매우 높음
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
rice = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(max(rice), 0, -1):
    total = 0
    for j in rice:
        if j > i:
            total += (j-i)

    if total == m:
        print(i)
        break


# 이진탐색 풀이
# 적절한 H를 찾을 때까지 이를 반복하며 조정
# 탐색 범위가 1~10억으로 매우 크기 때문에 이진탐색으로 풀어야함
n, m = map(int, sys.stdin.readline().rstrip().split())
rice = list(map(int, sys.stdin.readline().rstrip().split()))
rice.sort()

start = 0
end = max(rice)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in rice:
        if i > mid:
            total += i-mid
    if total<m:  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        end = mid-1
    else:  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid+1

print(result)
