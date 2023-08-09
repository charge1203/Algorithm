def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2

    answer = numbers

    return answer

# 다른 답안
def solution1(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer

def solution2(numbers):
    return [num*2 for num in numbers]

def solution3(numbers):
    return list(map(lambda x: x * 2, numbers))