# 실버2
# 딕셔너리만 잘하면 됨
# get 메소드
# 두 번째 인자로는 첫 번째 인자에서 넣은 키가 없을 때 넣고자 하는 값을 넣는다
# items 메소드
# 딕셔너리의 키, 값 쌍 얻기

import sys

input = sys.stdin.readline

dic = dict()
count = 0

while True:
    s = input().rstrip()
    if not s:
        break
    dic[s] = dic.get(s,0)+1  # 여기!!!!
    count += 1

for k,v in sorted(dic.items()):
    ratio = round(v/count*100,4)
    print('%s %.4f' %(k,ratio))