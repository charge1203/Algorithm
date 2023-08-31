# 조금 조잡함
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ',')
    my_string = my_string.split(',')
    for i in my_string:
        if i == '':
            continue
        else:
            answer += int(i)
    return answer


# 다른풀이
# 내 의도랑 비슷하지만 더 간결
def solution2(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()

    return sum(list(map(int, my_string)))


# 라이브러리 이용 + 정규표현식 풀이
# re 라이브러리의 findall(): 주어진 패턴에 해당하는 내용들만 리스트로 만들어 즘
# 1번 이상 반복되는 정수를 의미하는 r'\d+'를 패턴
import re

def solution3(my_string):
    num = re.findall(r'\d+', my_string)  # r'[0-9]+'
    num = list(map(int, num))
    return sum(num)
