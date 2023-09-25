# 실버3
# 정렬
# 정렬로 안풀면 시간초과 뜸

# second try
# 투포인터 이용
# 좌, 우 방향의 인덱스를 이용하여 한 번의 배열 탐색으로 두 수의 합이 x가 되는 쌍을 찾을 수 있음
import sys
n = int(sys.stdin.readline().rstrip())
num = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
x = int(sys.stdin.readline().rstrip())
count = 0

left, right = 0, n-1 # 왼쪽, 오른쪽
while left < right:
    temp = num[left] + num[right]
    if temp == x:
        count += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(count)



# first try: 정렬로 안품
import sys
n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())
count = 0

for i in range(n):
    for j in range(i,n):
        if num[i]+num[j] == x:
            count += 1

print(count)