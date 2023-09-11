import sys
# from collections import deque
input = sys.stdin.readline

n = map(int, input().split())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

def dfs(i, now_num):
    global max_value, min_value, add, sub, mul, div
    # 연산자 다 쓰면 최솟값 최댓값 리턴
    if i == n:
        min_value = min(min_value, now_num)
        max_value = max(max_value, now_num)
    else:
        if add>0:
            add -= 1
            dfs(i+1, now_num+a[i])
            add += 1
        if sub>0:
            sub -= 1
            dfs(i+1, now_num-a[i])
            sub += 1
        if mul>0:
            mul -= 1
            dfs(i+1, now_num*a[i])
            mul += 1
        if div>0:
            div -= 1
            dfs(i+1, int(now_num/a[i]))
            div += 1

dfs(1,a[0])
print(max_value)
print(min_value)