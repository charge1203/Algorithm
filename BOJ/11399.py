n = int(input())  # 사람 수 입력 받기
p = list(map(int, input().split())) # 각 사람이 걸리는 시간 입력 받기

time = 0
p.sort() # 걸리는 시간 오름차순으로 정렬

for i in range(n):
    for j in range(i+1):
        time += p[j]

print(time)