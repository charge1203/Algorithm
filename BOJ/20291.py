# sys 안썼더니 시간 너무 오래 걸림 (10배 차이남)
# sys로 input 하는 법도 익히기!!!!1

import sys

n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    ex = sys.stdin.readline().rstrip().split('.')[1]  # 굳이 name 저장할 필요 없음
    if ex not in dic:
        dic[ex] = 1
    else:
        dic[ex] += 1

dic = dict(sorted(dic.items(), reverse=False)) # 딕셔너리 sort 주의

for key, value in dic.items():  # 딕셔너리에서 key value 모두 출력해야하니
    print(key, value)
