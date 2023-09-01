# 등수 매기는 코드 잘 못짬
def solution(score):
    answer = []
    ave = []
    for i in score:
        ave.append(float(sum(i)/2))
    answer = [sorted(ave, reverse=True).index(i)+1 for i in ave]  # 순위 코드 잘 못짬
    return answer


# 다른풀이
def solution2(score):
    answer = []
    result = []
    for n in score:
        answer.append(sum(n) / len(n))

    sort_arr = sorted(answer, reverse=True)

    for i in answer:
        result.append(sort_arr.index(i) + 1)

    return result