# 다시풀기

def solution(sequence, k):
    l = r = 0  # 왼쪽, 오른쪽 인덱스
    answer = [0, len(sequence)]
    sum = sequence[0]  # 제일 첫 숫자를

    while True:
        if sum < k:
            r += 1  # 오른쪽 한 칸 더
            if r == len(sequence): break
            sum += sequence[r]
        else:
            if sum == k:
                if r-l < answer[1]-answer[0]:
                    answer = [l, r]
            sum -= sequence[l]  # sum이 k보다 크면
            l += 1  # 왼쪽거 땡기기
    return answer