def solution(dot):
    answer = 0

    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        elif dot[1] < 0:
            answer = 4
    elif dot[0] < 0:
        if dot[1] > 0:
            answer = 2
        elif dot[1] < 0:
            answer = 3

    return answer

# 다른 풀이
def solution1(dot):
    if dot[0] >0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] >0:
        return 2
    elif dot[0] <0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] <0:
        return 4

def solution2(dot):
    a, b = 1, 0
    if dot[0]*dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2*a-b

def solution3(dot):
    x,y = dot
    if x*y>0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2