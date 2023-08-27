# 코드 진짜 별로다..

def solution(my_string):
    answer = []
    for i in my_string:
        if i in answer:
            my_string.replace(i, '')
            continue
        answer.append(i)

    string = ''
    for i in answer:
        string += i

    return string

# 다른풀이
# dict.fromkeys(key,value)
# key, value 값을 부여한 딕셔너리 값을 만들 수 있음
# 리스트의 중복을 제거할 때 사용 가능
def solution2(my_string):
    return ''.join(dict.fromkeys(my_string))

# 다른풀이
def solution3(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer