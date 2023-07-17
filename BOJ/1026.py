n = int(input())  # N 입력 받기

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

s = 0
a_list.sort()
for i in range(n):
    x = a_list[i]
    y = b_list.pop(b_list.index(max(b_list)))

    s += x * y

print(s)