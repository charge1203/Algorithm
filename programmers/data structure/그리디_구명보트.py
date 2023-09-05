# first try
# 정확성 통과 but 효율성 0점
# pop()은 리스트의 마지막 인덱스에서 해당 인덱스를 찾아가기 때문에 시간 복잡도가 O(1)인 반면
# pop(n)은 리스트 자체를 통으로 복사하는 과정이 들어가고 인덱스를 찾는 과정까지 들어가서 O(n)의 시간 복잡도를 가진다.
def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    while people:
        i = 0
        if people[0]+people[-1] > limit:
            people.pop(0)
            answer += 1
        else:
            people.pop(0)
            if not people:
                answer += 1
                break
            people.pop()
            answer += 1
    return answer

# second try
# sort를 안하였지만 여전히 효율성 0점..
def solution2(people, limit):
    answer = 0
    while people:
        i = 0
        if max(people)+min(people) > limit:
            people.pop(people.index(max(people)))
            answer += 1
        else:
            people.pop(people.index(max(people)))
            if not people:
                answer += 1
                break
            people.pop(people.index(min(people)))
            answer += 1
    return answer


# 얘의 답은 큐를 써야하는 거였음
# 논리는 맞았는데, 큐를 안써서 효율성이 0이 되다니.....
from collections import deque

def solution3(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    while len(people)>1:
        i = 0
        if people[0]+people[-1] <= limit:
            people.popleft()  # 최대 빼냄
            people.pop()  # 최소 빼냄
            answer += 1
        else:
            people.popleft()
            answer += 1
    if people: # 한 명 남아있을 경우
        answer += 1
    return answer


# 다른 풀이
def solution4(people, limit) :
    answer = 0
    people.sort()

    # 인덱스를 start, end 시점을 투 포인터 이용
    a = 0  # 값 작은 애의 인덱스
    b = len(people) - 1  # 값 큰 애의 인덱스
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1  # 두 명이 한 보트인 경우
        b -= 1
    return len(people) - answer