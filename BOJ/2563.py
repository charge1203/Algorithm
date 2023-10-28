n = int(input())
paper = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화
for _ in range(n):
    y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.
    for i in range(x1, x1 + 10):  # 세로를 돈다.
        for j in range(y1, y1 + 10):  # 가로를 돈다.
            paper[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

result = 0
for k in range(100):
    result += paper[k].count(1)

print(result)