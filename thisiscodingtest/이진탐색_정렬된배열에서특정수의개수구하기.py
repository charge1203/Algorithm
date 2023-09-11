# 계수 정렬 이용
n,x = map(int, input().split())
num = list(map(int, input().split()))

radix = [0]*(max(num)+1)

for i in num:
    radix[i] += 1

if x in num:
    print(radix[x])
else:
    print(-1)

# 이진탐색
# bisect 메소드 이용한거나 정리할래
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index-left_index

n,x = map(int, input().split())
num = list(map(int, input().split()))

count = count_by_range(num, x,x)

if count ==0:
    print(-1)
else:
    print(count)