# 구현
# 실버2

import sys

n = int(sys.stdin.readline().rstrip())
tall = list(map(int, sys.stdin.readline().rstrip().split()))

seq = [0] * n

for i in range(n):
    zero_list = [i for i in range(len(seq)) if seq[i]==0]  # seq에서 값이 0인 인덱스 반환
    seq[zero_list[tall[i]]] = i+1  # 0이 tall[i]개 만큼 있을 때 zero_list의 tall[i]개 후의 자리에 내 번호 입력

for i in seq:
    print(i, end=' ')