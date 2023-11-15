# DP
# 다시풀어보기!!!!

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 현재 줄이 j인데 j는 빼고 land[i-1][:j]와 land[i-1][j+1:] 리스트 원소 한꺼번에 한 것 중 가장 큰거를 더해주기
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[len(land) - 1]) # 막줄에서의 최대