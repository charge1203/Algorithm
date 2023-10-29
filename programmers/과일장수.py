def solution(k, m, score):
    boxes = []
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        boxes.append(score[i:i+m])
    for box in boxes:
        if len(box) == m:
            answer += min(box) * m
    return answer