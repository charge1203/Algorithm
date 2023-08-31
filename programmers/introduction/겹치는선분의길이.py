# 조잡한 나의 코드....
def solution(lines):
    answer = []
    for i in range(len(lines)):
        for j in range(lines[i][0], lines[i][1]):
            for k in range(lines[(i+1)%3][0],lines[(i+1)%3][1]):
                if j == k:
                    answer.append(j)
    return len(set(answer))

# 다른풀이
def solution(lines):
    # 집합으로 각 선분 안의 값을 불러오기
    sets = [set(range(min(l), max(l))) for l in lines]
    # 각 선분끼리의 교집합을 구하고 각각의 교집합의 합집합의 길이를 반환
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])