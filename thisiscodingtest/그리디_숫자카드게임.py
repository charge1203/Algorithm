# 각 행마다 가장 작은 수를 찾은 뒤에 그 수들 중에서 가장 큰 수 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = []
a = []

for i in range(n):
    card.append(list(map(int, input().split())))

for i in range(len(card)):
    a.append(min(card[i]))

print(max(a))


# 다른 풀이
n, m = map(int, input().split())
result = 0

for i in range(n):  # 각 행에 대하여
    data = list(map(int, input().split()))  # 한 줄씩 입력 받기
    min_value = min(data)  # min() 함수 이용하여 현재 행에서 가장 작은 수 찾기
    result = max(result, min_value)  # 현재 행에서 찾은 가장 작은 수와 저장되어있던 result 값 중 큰 값 찾기

    print(result)