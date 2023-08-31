# 다시해보기
def solution(dots):
    answer = 0
    if slope(dots[0],dots[1]) == slope(dots[2],dots[3]):
        answer = 1
    if slope(dots[0],dots[2]) == slope(dots[1],dots[3]):
        answer = 1
    if slope(dots[0],dots[3]) == slope(dots[1],dots[2]):
        answer = 1
    return answer

def slope(dot1,dot2):
    return (dot2[1] - dot1[1] ) / (dot2[0] - dot1[0]) # 기울기 계산 (y축 차이 - x축 차이)


# 다른풀이
from itertools import combinations

def solution2(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))

    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2==x2*y1:
            return 1
    return 0