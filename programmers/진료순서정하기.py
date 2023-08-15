def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse=True)

    # 정렬한 tmp리스트에서 알고싶은 emergency요소를 넣어서 인덱스를 가져온다. 즉 순위를 가져온다.
    for i in emergency:
        answer.append(tmp.index(i) + 1)

    return answer