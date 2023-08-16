def solution(age):
    answer = ''
    return answer.join([chr(int(i)+97) for i in str(age)])


def solution2(age):
    answer = ''
    word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in str(age):
        answer += word[int(i)]
    return answer
