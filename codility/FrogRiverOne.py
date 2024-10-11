# 간단히 정리하면 1부터 X까지 모든 자연수가 등장했을 때의 인덱스를 구하라는 문제

def solution(X, A):
    nums = set()  # 집합 만들고
    for i in range(len(A)):
        nums.add(A[i])  # 집합은 add
        if len(nums) == X:
            break

    if (i==len(A)-1) and len(nums) != X:
        return -1

    return i