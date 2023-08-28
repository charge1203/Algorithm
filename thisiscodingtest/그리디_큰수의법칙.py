import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
num = list(map(int, input().split()))

# 데이터 정렬할 생각을 안했음
num.sort()
first = num[-1:]  # 리스트에서 마지막
second = num[-2:-1]  # 리스트에서 마지막에서 두번째
# num[n-1], num[n-2]로 했어도 됨

result = (first * k + second) * (m//(k+1)) + first * (m%(k+1))

print(sum(result))