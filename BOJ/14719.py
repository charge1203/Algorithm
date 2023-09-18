# 골드5
# 구현
# 해설 보고 함 -> 아이디어 떠올리지 못함
# 왼쪽과 오른쪽을 탐색해 두 방향 모두에서 더 높은 블록에 둘러 쌓여있으면 빗물이 고임

import sys
h, w = map(int, sys.stdin.readline().rstrip().split())
blocks = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0  # 빗물의 고인 양
for i in range(1, w - 1):  # 맨 왼쪽과 맨 오른쪽은 고일 수 없음
    left_max = max(blocks[:i])  # 왼쪽에서 제일 높은 블록
    right_max = max(blocks[i + 1:])  # 오른쪽에서 제일 높은 블록

    lower_one = min(left_max, right_max)  # 그중 가장 낮은 블록

    if blocks[i] < lower_one:  # 현재 블록이 lower_one 블록 보다는 낮아야 빗물이 고임
        result += lower_one - blocks[i]
print(result)