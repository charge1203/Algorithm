# 맞았지만 조금 조잡함
def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        if i == 'left':
            if answer[0] != -(board[0] // 2):
                answer[0] -= 1
        elif i == 'right':
            if answer[0] != (board[0] // 2):
                answer[0] += 1
        elif i == 'up':
            if answer[1] != (board[1] // 2):
                answer[1] += 1
        elif i == 'down':
            if answer[1] != -(board[1] // 2):
                answer[1] -= 1

    return answer


# 다른풀이
def solution2(keyinput, board):
    x_boundary = board[0] // 2
    y_boundary = board[1] // 2
    result = [0,0]
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(x_boundary):
            result[0]-=1
        elif i == "right" and result[0]+1 <= (x_boundary):
            result[0] += 1
        elif i == "up" and result[1] +1 <= (y_boundary):
            result[1] += 1
        elif i == "down" and result[1] -1 >= -(y_boundary):
            result[1] -= 1
    return result