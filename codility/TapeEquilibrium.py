# for문 안에 sum을 없애자

def solution(A):
    min_sum = 100000
    left = 0
    right = sum(A)

    for i in range(len(A) - 1):
        left += A[i]
        right -= A[i]
        min_sum = min(min_sum, abs(left - right))

    return min_sum