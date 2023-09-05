# try는 밑에 있음

# 우선순위큐로 풀어야했대...
# 다시 이해하기
import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

result = 0

if len(cards) == 1:
    print(result)  # 비교할 필요가 없으므로

else:
    for i in range(n - 1):  # 2개씩 꺼내기 떄문에 n-1
        previous = heapq.heappop(cards)
        current = heapq.heappop(cards)

        result += previous + current
        heapq.heappush(cards, previous + current)

    print(result)


# first try
# 출력 초과 뜸
import sys

n = int(sys.stdin.readline())
card = []
sum = 0

for _ in range(n):
    card.append(int(sys.stdin.readline()))

card.sort()

for i in range(len(card)):
    if i <2:
        sum += card[i]
    else:
        sum += sum + card[i]

print(sum)

