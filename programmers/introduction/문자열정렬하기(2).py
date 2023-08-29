def solution(my_string):
    answer = []
    a = ''
    for i in my_string:
        if i.isupper():
            answer.append(i.lower())
        else:
            answer.append(i)

    for i in sorted(answer):
        a += i
    return a


# 다른풀이
def solution2(my_string):
    answer = ''
    for i in my_string:
        answer += i.lower()
    return ''.join(sorted(answer))  # 이렇게 리스트 정리하는 것도,,

# 다른풀이
# 시간복잡도 상당히 줄임
def solution3(my_string):
    return ''.join(sorted(my_string.lower()))