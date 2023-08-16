def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers[len(numbers) - 1])
        numbers.pop()

    elif direction == 'left':
        numbers.insert(len(numbers), numbers[0])
        del numbers[0]

    return numbers


# 다른 풀이
# deque 사용
# deque의 rotate 함수 안에 음수를 넣으면 왼쪽 회전, 양수는 오른쪽 회전
from collections import deque
def solution1(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    elif direction == 'left':
        numbers.rotate(-1)

    return list(numbers)

# 또 다른 풀이
# 주의할 점은 리스트 크기 하나짜리는 그냥 슬라이싱하면 숫자만 나와지기 때문에 리스트 안에 넣어서 리스트끼리 + 연산자
def solution2(numbers, direction):
    if direction == 'right':
        return [numbers[-1]] + numbers[:len(numbers)-1]
    elif direction == 'left':
        return numbers[1:] + [numbers[0]]