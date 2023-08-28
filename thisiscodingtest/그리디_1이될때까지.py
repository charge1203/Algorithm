import sys

n, k = map(int, sys.stdin.readline().split())
count = 0

while n!=1:
    if n % k == 0:
        n = n/k
        count += 1
    else:
        n -= 1
        count +=1

print(count)

# 흠.. 코드 잘 짠건가..


# 다른풀이
# N이 K의 배수가 되도록 한 번에 빼는 방식의 코드

n, k = map(int, input().split())
result = 0

while True:
    # N == (K로 나누어 떨어지는 수) 될 때까지 1 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:  # N이 K보다 작아 더 이상 나눌 수 없을 때
        break  # 반복문 탈출

    result += 1
    n //= k

result += (n - 1)  # 마지막으로 남은 N에 대하여 1 빼기
print(result)