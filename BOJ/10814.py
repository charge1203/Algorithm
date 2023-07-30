n = int(input())
info = []

for _ in range(n):
    age, name = input().split()
    info.append([int(age), name])

info.sort(key=lambda x:int(x[0]))

for i in range(n):
    print(info[i][0], info[i][1])

