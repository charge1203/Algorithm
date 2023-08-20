def solution(my_string):
    gather = ['a', 'e', 'i', 'o', 'u']
    for i in gather:
        my_string = my_string.replace(i, '')
    return my_string

# 다른풀이
def solution2(my_string):
    answer = ''
    letter = ['a', 'e', 'i', 'o', 'u']

    # letter와 다른 문자열만 answer에 저장
    for i in my_string:
        if i != letter:
            answer += i

    return answer

# 다른풀이
# 리스트 컴프리헨션 이용
def solution3(my_string, letter):
    answer = ''.join([i for i in my_string if i not in letter])
    return answer