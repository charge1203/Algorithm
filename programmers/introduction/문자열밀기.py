# 못 푼 문제... A를 미는건데 B를 밀어서 그런듯

def solution(A, B):
    answer = -1

    ## 처음부터 A와 B가 같으면
    if A == B:
        return 0

    for i in range(1, len(A)):
        ## A를 오른쪽으로 한 칸씩 밀었을때
        A = A[-1] + A[0:-1]
        print(A)
        if A == B:
            return i

    return answer


