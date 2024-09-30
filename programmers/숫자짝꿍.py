def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):  # 9~0까지 X, Y에서의 개수 세기
        countX = X.count(str(i))
        countY = Y.count(str(i))
        if (countX != 0 and countY != 0):  # 숫자i의 개수가 X와 Y에서 모두 0개가 아니면
            if (len(answer) == 0) and (i == 0):  # i가 0이고 중복숫자의 길이가 0이면 (중복 숫자가 없으면)
                answer = '0'
            else:
                result = countX if (countX < countY) else countY  # 더 작은쪽의 개수 저장하고
                for _ in range(result):  # 그 횟수만큼
                    answer += str(i)  # 그 숫자 i 저장

    if (len(answer) == 0):  # 중복 숫자가 없다면
        answer = '-1'

    return answer