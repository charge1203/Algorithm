def solution(quiz):
    answer = []
    for i in quiz:
        a = i.split(' ')
        if a[1] == '+':
            result = int(a[0])+int(a[2])
        elif a[1] == '-':
            result = int(a[0])-int(a[2])
        if int(a[-1]) == result:
            answer.append('O')
        else:
            answer.append('X')
    return answer


# 다른풀이
# eval
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution2(equations):
    return ["O" if valid(equation) else "X" for equation in equations]

# 다른 풀이
def solution3(quiz):
    answer = []
    for i in quiz:
        if eval(i.split('=')[0]) == int(i.split('=')[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer