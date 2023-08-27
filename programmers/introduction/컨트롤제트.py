def solution(s):
    answer = 0
    s = s.split(' ')

    for i in range(len(s)):

        if s[i] == 'Z':
            answer -= int(s[i - 1])
            continue
        else:
            answer += int(s[i])

    return answer


# 다른 풀이
def solution2(s):
    stack = []
    for num in s.split(' '):
        try:  # num이 숫자일 경우 stack에 append
            stack.append(int(num))
        except:  # 숫자가 아닌 Z일 경우 바로 pop을 이용해 바로 전에 append 해준 숫자를 stack에서 뺌
            stack.pop()
    return sum(stack)