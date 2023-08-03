# 브루트포스: 완전 탐색 알고리즘
# 가능한 모든 수를 조합하는 방식
# 666, 1666, 2666, 3666... 6661, 6662, ...
# 반복문 안에는 조건문을 통해 result 값에 '666'이 포함하는지를 판단하여 '666'이 포함되어 있을 경우 count를 1씩 증가

n = int(input())
count = 0  # 몇 번째 666인지
first = 666

while n != 0:
    if '666' in str(first): # 666이 first라는 문자열 내에 있다면
        count += 1

    if count == n:
        break

    first += 1  # 666 다음 숫자 탐색

print(first)



