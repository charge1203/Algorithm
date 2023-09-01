# 정답률 제일 낮긴 했는데 맞음!
import itertools
def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    nPr2 = itertools.permutations(word, 2)
    nPr3 = itertools.permutations(word, 3)
    nPr4 = itertools.permutations(word, 4)
    for i in list(nPr2):
        word.append(i[0]+i[1])
    for i in list(nPr3):
        word.append(i[0]+i[1]+i[2])
    for i in list(nPr4):
        word.append(i[0]+i[1]+i[2]+i[3])

    for i in babbling:
        if i in word:
            answer += 1
    return answer

# 다른풀이
# 나랑 비슷하지만 좀 더 깔끔
from itertools import permutations
def solution2(babbling):
    answer = 0
    speek = ["aya","ye","woo","ma"]
    word = []
    for i in range(1, len(speek)+1):
        for j in permutations(speek, i):
            word.append(''.join(j)) # 이렇게 붙이면 되네

    for i in babbling:
        if i in word:
            answer += 1

    return answer