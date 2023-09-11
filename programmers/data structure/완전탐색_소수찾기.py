# 어렵네..
import itertools

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers) + 1):
        per += list(itertools.permutations(nums, i))
    new_nums = set([int(("").join(p)) for p in per])  # 각 순열조합을 하나의 int형 숫자로 변환
    # print(new_nums)

    for i in new_nums:
        if is_prime_number(i):
            answer.append(i)
    # print(answer)
    return len(answer)
