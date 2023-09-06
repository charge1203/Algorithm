# 모르겠어 어려워
# 다이나믹 프로그래밍 이용하여 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾는다

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
money = []

for _ in range(n):
    money.append(int(sys.stdin.readline().rstrip()))

d = [10001] * (m+1)  # 0~m까지 리스트에 10001 넣기
# 10001은 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 것

d[0] = 0
for i in range(n):  # 가능한 화폐 가치에 대해
    for j in range(money[i], m+1):  # 화폐가치가 제일 작은 것부터 만들어야하는 m까지
        if d[j-money[i]] != 10001:  # (만드려는 값-현재화폐가치)원을 만들 수 있을 떄
            d[j] = min(d[j], d[j-money[i]]+1)

# 결과
if d[m] == 10001: # m을 만들 수 없는겨
    print(-1)
else:
    print(d[m])