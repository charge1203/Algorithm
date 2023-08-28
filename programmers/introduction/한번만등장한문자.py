# 뭔가 초큼 조잡..

def solution(s):
    dic = {}
    answer = ''

    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    dic = dict(sorted(dic.items()))
    word = [k for k, v in dic.items() if v == 1]

    for i in word:
        answer += i

    return answer


# 다른 풀이
# 주어진 문자열에서 한 요소를 찾아가면서 count()함수를 사용했을 때 값이 1인 경우에 answer에 넣기
def solution2(s):
    answer = ''
    for i in s:
        if s.count(i)==1:
            answer += i
    return ''.join(sorted(answer))