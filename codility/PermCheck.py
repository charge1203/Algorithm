# O(N) or O(N * log(N))
def solution(A):
    A.sort()
    if A[-1]!=len(A) or A[0]!=1: return 0
    for i in range(len(A)-1):
        if A[i+1]-A[i] != 1:
            return 0
    return 1