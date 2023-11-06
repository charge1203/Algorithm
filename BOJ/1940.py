# 투포인터 사용
n = int(input())
m = int(input())
num = list(map(int, input().split()))

num.sort()
start = 0
end = len(num)-1
count = 0

while start < end:
    result = num[start] + num[end]
    if result > m:
        end -= 1
    elif result < m:
        start += 1
    else:
        count += 1
        start += 1
        end -=1

print(count)
