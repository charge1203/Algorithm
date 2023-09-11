# 이진탐색
n = int(input())
num = list(map(int, input().split()))
num.sort()

def binary_search(array,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid-1
        elif array[mid] < mid:
            start = mid+1
    return -1

answer = binary_search(num,0,n-1)

print(answer)



# 이렇게 하면 시간초과겠지
# n = int(input())
# num = list(map(int, input().split()))
#
# for i in range(n):
#     if num[i] == i:
#         print(i)
#         break
#     if i == n and num[n] != n:
#         print(-1)