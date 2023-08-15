def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()

    # lost, reserve에 공통으로 있는 요소 제거
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    # 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
    # 여기서 reserve[:]에서 [:] 쓰냐 안쓰냐에 따라 결과가 다름
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    return n - len(lost)