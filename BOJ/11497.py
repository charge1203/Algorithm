# 통나무 높이 차가 최소가 되게 정렬을 해야함
# 그 후 난이도가 가장 작은 것을 리턴
# 그리디 -> 가장 큰 것을 센터에 두고 양 옆으로 그 다음으로 큰거 배열
# n개의 통나무가 있을 때 인접하는 통나무 사이의 최대 높이차:
# 1번과 3번의 높이차, 2번과 4번의 높이차, ... n-2번과 n번의 높이차
# 1번과 2번, n-1번과 n번도 인접하지만,
# 이것들은 각각 1번과 3번의 높이차, n-2번과 n번의 높이차보다 작으므로 무시해도 좋다.

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    max_level = 0
    for i in range(2,n):
        max_level = max(max_level, abs(l[i]-l[i-2]))

    print(max_level)

