def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)  # ingredient의 요소 하나씩을 s 리스트에 넣어
        # 그러다가 뒤에서부터 4개가 1,2,3,1이면
        if s[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                s.pop()  # 4개 다 빼
    return answer


# first try -> 대부분 테케 시간초과
def solution1(ingredient):
    answer = 0
    hambug = [1,2,3,1]
    while True:
        for i in range(len(ingredient)-len(hambug)+1):
            if ingredient[i:i+4] == hambug:
                del ingredient[i:i+4]
                answer += 1
                break
        else:
            break
    return answer