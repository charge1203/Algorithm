import sys

s = sys.stdin.readline().rstrip()
answer = int(s[0])
for i in s[1:]:
    if answer == 0:
        answer += int(i)
        continue

    if i == '0':
        answer += int(i)
    elif i != '0':
        answer *= int(i)

print(answer)


# 다른 풀이
# 연산하는 두 수 중 하나라도 1 이하일 때는 연산자 '+' 선택, 그 외의 경우는 'x' 연산자 선택
s = input()  # 문자열 입력 받음

result = int(s[0])  # 첫번째 인덱스의 문자를 숫자로 변경하여 대입

for i in range(1, len(s)):
    num = int(s[i])  # i번째 문자를 숫자로 변경하여 대입
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)