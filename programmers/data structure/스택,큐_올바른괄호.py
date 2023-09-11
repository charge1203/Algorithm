# first try
# 정확성 일부, 효율성 반 틀림 (73.2점)
def solution(s):
    answer = []
    if s[-1] == '(':
        return False
    for i in s:
        if not answer:
            answer.append(i)
        if i == '(':
            answer.append(i)
        elif i == ')':
            if answer[-1] == '(':
                answer.pop()
            else:
                return False
    return True


# second try 답안 참고함
def solution2(s):
    answer = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            answer.append(i)
        else:  # i == ')'인 경우
            if not answer:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                answer.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
    if answer:  # 다 돌았는데 스택에 '('가 남아있다면
        return False
    return True

