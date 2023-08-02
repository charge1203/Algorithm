# deque 이용
# deque: 스택, 큐의 기능을 모두 가짐
# 스택 구현(마지막(오른쪽 끝)에서 입출력): append(), pop() 마지막(오른쪽 끝)에서 입출력
# 큐 구현(처음(왼쪽)에서 입력, 마지막에서 출력: appendleft(), pop()
# 처음에서 값 빼기(출력): popleft()
# deque 확장: extend(), (왼쪽에서 확장): extendleft()
# 리스트처럼 사용: insert()(인덱스 사용), remove()(같은 항목이 있을 때는 왼쪽부터 제거됨)
# 좌우 반전: reverse()

from collections import deque

def solution(n, m, section):
    answer = 0  # 페인트를 칠해야하는 최소 횟수
    section = deque(section)  # 앞에서부터 차례로 칠하기 위해 데큐 선언

    # 페인트 칠을 전부다 할 때까지 반복
    while section:
        start = section.popleft()  # 페인트칠 시작 지점

        while section and start + m > section[0]:  # 여기서 section도 추가해야하는 이유는 뭘까
            section.popleft()
        answer += 1

    return answer