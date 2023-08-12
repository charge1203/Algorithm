# 계속 시간 초과 문제 발생
# sys 모듈 사용 -> 그럼에도 시간 초과 문제 발생
# 리스트 사용하여 name append/remove 했을 때 시간 초과 문제 발생
# 딕셔너리 사용하였더니 시간초과 문제 해결

import sys

n = int(sys.stdin.readline())
dict={}

for _ in range(n):
    name, cg = map(str, sys.stdin.readline().split())
    if cg == 'enter':
        dict[name] = 'enter'
    elif cg == 'leave':
        del dict[name]

dict = sorted(dict.keys(), reverse=True)

for i in dict:
    print(i)