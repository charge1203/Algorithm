def solution(n):
    answer = 0
    one_count = bin(n).count('1')
    for i in range(n+1, 1000001):
        i_one_count = bin(i).count('1')
        if one_count == i_one_count:
            answer = i
            break
    return answer