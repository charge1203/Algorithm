def solution(my_string):
    lst = list(my_string)
    lst.reverse()
    answer = ''.join(lst)
    return answer


def solution2(my_string):
    reverse_string = ''

    for i in my_string:
        reverse_string = i + reverse_string

    return reverse_string
