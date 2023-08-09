def solution(array):
    dict = {}
    answer = 1

    for i in array:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1

    mx = [k for k, v in dict.items() if max(dict.values()) == v]
    # 이 부분 코드 짜는데 어려웠음
    # 딕셔너리의 값이 최대인 키값들을 리스트에 저장

    if len(mx)==1:
        answer = mx[0]
    else:
        answer = -1

    return answer

# 다른 솔루션
def solution1(array):
    count = [0] * (max(array) + 1)  # 숫자 출연 횟수를 셀 리스트

    for i in array:
        count[i] += 1

    m = 0  # 최빈값의 개수
    for c in count:
        if c == max(count):
            m += 1

    if m > 1:  # 최빈값이 2개 이상이면 -1을 리턴
        return -1
    else:  # 최빈값이 1개이면 해당 숫자를 리턴
        return count.index(max(count))


def solution2(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1