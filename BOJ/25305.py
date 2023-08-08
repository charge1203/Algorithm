n, k = map(int, input().split())
x = list(map(int, input().split()))  # 이부분 틀렸었음

x.sort(reverse=True)  # 내림차순하기
print(x[k-1])