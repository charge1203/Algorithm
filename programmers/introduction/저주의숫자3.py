# 상당히 맘에 안듦
def solution(n):
    lst = []
    for i in range(1,n*3):
        if i%3 != 0 and '3' not in str(i):
            lst.append(i)
    print(lst)
    return lst[n-1]

# 다른풀이
def solution2(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer):
            answer += 1  # 3의 배수이거나 3을 포함하면 1을 한 번 더 추가
    return answer