# 최초로 마이너스가 나오기 전까지는 더하기 ( - (최댓값)을 하기 위함)
# 뭉텅이 - 뭉텅이 - 뭉텅이 할 속셈
# 뭉텅이는 숫자 단일일 수도 있고 + 연산자로 이어진 긴 식일 수도 있음

exp = input().split('-')  # - 연산자 기준으로 split
result = 0

for i in exp[0].split('+'):
    result += int(i)

for i in exp[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)