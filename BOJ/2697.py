# 실버2
# 다시 풀어보기

import sys
for _ in range(int(sys.stdin.readline())):
    num = list(map(int, list(sys.stdin.readline().rstrip())))
    length, idx = len(num), 0
    # 여기도 더 이해해보기
    for i in range(length-1,0,-1):
        if num[i] > num[i-1]: # 뒤쪽 숫자가 앞보다 크다면
            if i == length-1:  # 그 때 i가 맨 뒤라면
                idx = length-2  # 인덱스는 그 앞으로
            else:
                idx = i-1  # 인덱스 한칸 앞으로
            break

    a = num[:idx]
    b = num[idx:]

    if not a or not b:  # 둘 중에 하나라도 비어있다면
        print('BIGGEST')
    else:
        b.sort()  # 뒤 쪽을 sort
        # 이 부분 이해하기
        for i in range(len(b)):
            if b[i]>num[idx]:
                a.append(b.pop(i))
                a.extend(b)
                break
        print(''.join(map(str, a)))