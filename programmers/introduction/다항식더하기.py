# first try 실패 -> 한자리수 넘는 x 계수일 때, x 계수가 1일 때, 상수항이 0일 때
# 너무 더럽게 푼 느낌이 있음. 가능한 경우 어거지로 다 만든 느낌
def solution(polynomial):
    answer = ''
    xs = 0
    integer = 0
    pol = polynomial.split(' + ')
    for i in pol:
        if 'x' in i:
            if len(i) == 1:
                xs += 1
            else:
                xs += int(i[:-1])  # 첫번째가 아닌 x빼고 다
        else:
            integer += int(i)

    if xs == 0:
        answer = str(integer)
    elif xs == 1:
        if integer != 0:
            answer = 'x' + ' + ' + str(integer)
        else:
            answer = 'x'
    elif integer == 0:
        answer = str(xs) + 'x'
    else:
        answer = str(xs) + 'x' + ' + ' + str(integer)

    return answer


# 다른풀이
def solution2(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'