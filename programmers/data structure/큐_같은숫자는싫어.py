# 스택 이용해보자
def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
        elif answer[-1] == i:
            pass
        elif answer[-1] != i:
            answer.append(i)
    return answer


# 다른풀이
def solution2(arr):
    ans = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
    return ans