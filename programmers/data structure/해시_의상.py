# 의상 종류를 카운트해서 안입음, 1번옷 입음, 2번 옷 입음 ... 으로 생각하여 각 의상 종류의 개수+1을 하여 곱한다
# 그 후 적어도 하나 이상을 입어야하므로 모두를 안입을 경우의 수인 1을 뺀다.

def solution(clothes):
    dict = {}
    answer = 1

    for cloth in clothes:
        if cloth[1] in dict.keys():
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1

    for value in dict.values():
        answer *= (value + 1)

    # 아무것도 입지 않은 경우 하나 제외
    return answer - 1
