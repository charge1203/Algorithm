n = int(input())
num = []  # 시리얼 정보를 담을 리스트

for i in range(n):
    num.append(input())

num.sort()
num.sort(key=lambda x: (len(x), sum(int(a) for a in x if a.isnumeric())))

for k in num:
    print(k)