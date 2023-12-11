import sys
input = sys.stdin.readline

n, l = map(int,input().split())
data = list(map(int, input().split()))
data.sort()

start = data[0]
count = 1

# 새는 곳 위치
for i in data[1:]:
    if i in range(start, start+l):  # 범위 내에 물 새는 곳 있다면
        continue # 기존 테이프 사용
    else:  # 새 테이프 사용
        start = i
        count += 1

print(count)