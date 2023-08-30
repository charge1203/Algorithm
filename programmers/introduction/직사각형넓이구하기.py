def solution(dots):
    # max를 dots에 묶고 거기서 [0]
    answer = (max(dots)[0]-min(dots)[0]) * (max(dots)[1]-min(dots)[1])
    return answer

# 다른풀이
def solution2(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    w = max(x) - min(x)
    h = max(y) - min(y)
    return w*h
