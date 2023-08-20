# 한 번에 풀지 못함

def solution(n):
    answer = []
    d = 2  # 소인수는 2부터
    while d <= n:
        if n % d == 0:
            answer.append(d)
            n = n // d
        else:
            d += 1
    return sorted(list(set(answer)))