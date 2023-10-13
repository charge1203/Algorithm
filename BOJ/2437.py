# 골드2

import sys

n = int(sys.stdin.readline().rstrip())
weight = list(map(int, sys.stdin.readline().rstrip().split()))
weight.sort()
min = 1

for i in weight:
    if min < i:
        break
    min += i

print(min)

# 풀이
# 1,1,2,3,6,7,30 추가 주어졌을 때
# 현재 min 1
# min이 첫 번째 추보다 같거나 크다면 => min += 첫 번째 추로 갱신
# 갱신한 min이 두 번째 추보다 같거나 크다면 => min += 두 번쨰 추로 갱신
# 만약 min이 그 다음 추보다 작다면 => 그 min은 나올 수 없음