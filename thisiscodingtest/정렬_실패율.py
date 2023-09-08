# first try
# 런타임 에러
def solution(N, stages):
    fail = []
    answer = []
    for i in range(1, N + 1):
        cnt = 0  # stage 간 유저
        for j in stages:
            if j >= i:
                cnt += 1
        fail.append((i, stages.count(i) / cnt))
    fail = sorted(fail, key=lambda x: x[1], reverse=True)

    for i in fail:
        answer.append(i[0])

    return answer


# second try
# 코드 참고함
# 계수정렬 써야하네
def solution2(N, stages):
    answer = []
    st = [0] * (N + 2)  # N+1 스테이지까지 있으니
    dic = {}
    try_member = len(stages)  # 도전자수

    for i in stages:  # 각 스테이지마다 stage에 현재 있는 사람 수 넣어주기
        st[i] += 1

    for i in range(1, N + 1):
        if try_member == 0:  # 도전자가 없다면
            dic[i] = 0
            continue
        dic[i] = st[i] / try_member
        try_member -= st[i]  # 그 스테이지에 머물러있는 사람들 빼기

    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic)
    for i in dic:
        answer.append(i[0])

    return answer

    # dic부터의 코드를 이렇게 한 줄로...
    return sorted(dic, key=lambda x: dic[x], reverse=True)


# 이코테 제공 코드
def solution3(N, stages):
    answer = []
    length = len(stages)

    for i in range(1,N+1):
        count = stages.count(i)  # 해당 스테이지에 머물러있는 사람 수

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count/length
        answer.append((i,fail)) # 리스트에 스테이지 번호, 실패율 넣기
        length -= count

    answer = sorted(answer, key=lambda x:x[1], reverse=True)
    answer = [i[0] for i in answer]

    return answer
