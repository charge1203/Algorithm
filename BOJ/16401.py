m, n = map(int, input().split())  #m:조카수, n:과자수 입력받기
snack_len = list(map(int, input().split()))

start = 1
end = max(snack_len)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for l in snack_len:
        count += l // mid
    if count >= m:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1
print(result)