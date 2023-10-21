def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i) * (food[i]//2)
        if i == len(food)-1:
            half = answer
    answer += '0'
    answer += half[::-1]
    return answer