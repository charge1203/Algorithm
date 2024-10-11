def solution(N):
    bin_n = format(N, 'b')  # 이진수로 변환

    # binary gap
    one_idx = []
    for idx, i in enumerate(bin_n):  # 1인거의 인덱스 저장
        if i == '1':
            one_idx.append(idx)

    if len(one_idx) < 2:
        return 0
    else:
        gap = []
        for i in range(len(one_idx)-1):
            gap.append(one_idx[i+1]-one_idx[i]-1)
        return max(gap)