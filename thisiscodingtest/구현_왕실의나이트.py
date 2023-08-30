# 다시 풀어보기

import sys

input_loc = sys.stdin.readline()

# ord(): 괄호( ) 안에 문자를 넣으면 그 문자에 해당하는 아스키코드를 숫자로 반환
x = int(input_loc[1])
y = int(ord(input_loc[0])) - int(ord('a')) + 1
count = 0

#나이트가 이동할 수 있는 8가지 방향
steps = [(-2,1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

for i in steps:
    nx = x + i[0]
    ny = y + i[1]

    # 해당 (nx,ny)에 이동 가능한지 확인
    if nx>=1 and nx<=8 and ny>=1 and ny<=8:
        count += 1

print(count)