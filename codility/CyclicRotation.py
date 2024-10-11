# first try
# 87점
# empty array일 때 run time error
def solution(A, K):
    for _ in range(K):
        A.insert(0, A[-1])
        A.pop()
    return A


# 테케 진짜 별의 별것 다 넣어봐야겠다
def solution2(A, K):
    if not A:
        return A

    for _ in range(K):
        A.insert(0, A[-1])
        A.pop()
    return A

# 슬라이싱 이용 풀이
def solution3(A, K):
    N = len(A)
    if N < 2:
        return A
    if K >= N:
        K = K%N
    return A[N-K:] + A[:N-K]

