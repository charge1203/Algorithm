# 문자열 수정은 리스트로 변환하여 수정

def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num1] = my_string[num2]
    answer[num2] = my_string[num1]

    # 이렇게 한 줄로 해도 됨
    # answer[num1], answer[num2] = my_string[num2], my_string[num1]
    return ''.join(answer)