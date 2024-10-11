# time complexity:O(N) or O(N*log(N))

def solution(A):
    if len(A) == 1:
        return A[0]

    A.sort()

    for i in range(0, len(A), 2):
        if i + 1 == len(A):  # 마지막 원소라면
            return A[-1]
        if A[i] != A[i + 1]:
            return A[i]