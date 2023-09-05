# 다시 풀어봐야함

def solution(genres, plays):
    dic1 = {}
    dic2 = {}
    answer = []
    for i, (g, p) in enumerate(zip(genres, plays)):  # 이렇게 한꺼번에 묶을 딕셔너리 생각하지 못함...
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer