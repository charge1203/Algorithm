# 구현
# 틀렸었었음

import sys

n = int(sys.stdin.readline())
card = [0] * 10  # 각 숫자별 나온 횟수를 카운트할 리스트
for i in str(n):
    if i == "9" or i == "6":
        if card[6] == card[9]:
            card[6] += 1
        else:
            card[9] += 1
    else:
        card[int(i)] += 1

print(max(card))