# first try -> score 22 (mistake)
# and develop -> score 100

def solution(X, Y, D):
    if (Y-X)%D == 0:
        return (Y-X)//D  # /이 아닌 // 써야함
    else:
        return (Y-X)//D + 1


# sol2 -> score 100
from math import ceil

def solution2(X, Y, D):
    return ceil(((Y-X)/D))