# first try
# score : 50
# 일부 runtime error
def solution(A):
    A.sort()
    for i in range(len(A)-1):
        if A[i]+1 != A[i+1]:
            return A[i]+1

# 케이스 잘 쪼개라
# O(N) or O(N * log(N))
def solution(A):
    if not A: return 1
    A.sort()
    if A[0] != 1: return 1
    for i in range(len(A)-1):
        if (A[i+1]-A[i]) != 1:
            return A[i]+1
    return A[-1] + 1


