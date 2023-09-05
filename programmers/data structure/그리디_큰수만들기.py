# 다시풀기 몇 번 try 해봤는데 못함
# stack (LIFO) 사용하라네
# 스택의 마지막 값이 push 할 값보다 작다면 크거나 같은 값이 나올 때까지 값들에 대해서 pop

def solution(number, k):
    answer = []  # 스택(LIFO) 늦게 들어온 애가 먼저 나감
    for i in number:
        if not answer:  # 스택이 비어있다면
            answer.append(i)
            continue
        if k > 0:
            while answer[-1] < i:  # 스택의 마지막 원소가 i보다 작다면
                answer.pop()  # 스택에서 뒤에 들어온 원소 뺴기
                k -= 1  # k count 줄여주기
                if not answer or k <= 0:  # (종료조건) 스택이 비어있거나 k가 0보다 작거나 같으면
                    break
        answer.append(i)

    answer = answer[:-k] if k > 0 else answer

    return ''.join(answer)