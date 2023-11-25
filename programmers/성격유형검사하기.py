def solution(survey, choices):
    answer = ''
    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for s, c in zip(survey, choices):
        if c > 4:
            score[s[1]] += c - 4
        elif c < 4:
            score[s[0]] += 4 - c

    lst = list(score.items())

    for i in range(0, 8, 2):
        if lst[i][1] >= lst[i + 1][1]:
            answer += lst[i][0]
        else:
            answer += lst[i + 1][0]
    return answer

# 런타임 에러
def solution3(survey, choices):
    answer = ''
    score = {'A' :0, 'N' :0, 'C' :0, 'F' :'0', 'J' :0, 'M' :0, 'R' :0, 'T' :0}
    for i in range(len(survey)):
        if choices[i] == 1:
            score[survey[i][0]] += 3
        elif choices[i] == 2:
            score[survey[i][0]] += 2
        elif choices[i] == 3:
            score[survey[i][0]] += 1
        elif choices[i] == 5:
            score[survey[i][1]] += 1
        elif choices[i] == 6:
            score[survey[i][1]] += 2
        elif choices[i] == 7:
            score[survey[i][1]] += 3
        elif choices[i] == 4:
            continue

    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'
    if int(score['C']) >= int(score['F']):
        answer += 'C'
    else:
        answer += 'F'
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer
