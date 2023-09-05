import sys

n = int(sys.stdin.readline().rstrip())
exist = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
need = list(map(int, sys.stdin.readline().rstrip().split()))
exist.sort() # sort 꼭 해야함!!!!!

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in need:
    result = binary_search(exist, i, 0, n)
    if result:  # != None 하면 되네
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 계수정렬 풀이
n = int(sys.stdin.readline().rstrip())
array = [0]*100001
# 가게에 있는 전체 부품 번호 입력받아 기록
for i in input.split():
    array[int(i)] = 1

# 손님
m = int(sys.stdin.readline().rstrip())
need = list(map(int, sys.stdin.readline().rstrip().split()))

for i in need:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 집합자료형 이용풀이
n = int(sys.stdin.readline().rstrip())
exist = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
need = list(map(int, sys.stdin.readline().rstrip().split()))

for i in need:
    if i in exist:
        print('yes', end=' ')
    else:
        print('no', end=' ')

