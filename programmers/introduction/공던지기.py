def solution(numbers, k):
    numbers = numbers*(k//int(len(numbers)/2)+1)
    return numbers[(k-1)*2]

# 맞았긴 하지만 마음에 들지 않음..

# 다른 풀이
# if 조건문으로 무분별하게 numbers 배열 뿔리는 일도 없고
# len(numbers)/2가 정수가 아닐 때 문제였는데 k를 2배하고 이를 len(numbers)로 나
# numbers 확장시켜야 할 경우
# k번을 두 칸씩 건너뛰어야 하므로 k*2가 len(numbers) 보다 클 때 확

def solution1(numbers, k):
    answer = 0
    if len(numbers) < k * 2:
        numbers = numbers * ((k*2) // len(numbers) + 1)

    answer = numbers[2*(k-1)]
    return answer


# 또 다른 풀이
# 배열을 확장시키지 않고 나머지 연산자 이용하여 기존 배열에서 순환하도록
# 1) 2칸씩 이동하므로 2를 곱해주고
# 2) 0번 인덱스부터 시작해서 '공을 던지는 사람'을 찾아야 하므로 (k-1)
# 3) numbers 길이를 넘어갈 수 없으므로 % 연산자 사용
def solution2(numbers, k):
    answer = numbers[2*(k-1) % len(numbers)]
    return answer
