import sys

n = sys.stdin.readline()
data = list(sys.stdin.readline().rstrip().split(' '))

loc = [1,1]
for i in data:
        if i == 'R':
            if loc[1] != 5:
                loc[1] += 1
        elif i == 'L':
            if loc[1] != 1:
                loc[1] -= 1
        elif i == 'U':
            if loc[0] != 1:
                loc[0] -= 1
        elif i == 'D':
            if loc[0] != 5:
                loc[0] += 1

print(loc[0], loc[1])


# 모범답안?
n = int(input())
x, y = 1, 1
plans = input().split()  # 입력 받은 것을 띄어쓰기 기준으로 나누기

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:  # 입력 받은 이동 계획에 따라 진행
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]  # 이동 후 좌쵸 구하기
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:  # 공간을 벗어나는 경우 무시
        continue

    x, y = nx, ny

print(x, y)