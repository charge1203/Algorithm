# 실버2

import sys
n = int(sys.stdin.readline().rstrip())
target = list(sys.stdin.readline().rstrip())
answer = 0


for _ in range(n-1):
    compare = target[:]
    word = sys.stdin.readline().rstrip()
    count = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            count += 1
    # count: target 단어에 포함되지 않은 word의 문자의 개수
    # compare에 남아있는 문자들: word에 포함되지 않은 문자들
    # count와 compare의 길이가 각각 1 이하여야만 조건을 만족하는 '비슷한 단어'
    if count < 2 and len(compare) < 2:
        answer += 1

print(answer)

