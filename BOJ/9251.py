# 동적 계획법 (dynamic programming): 하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장하여 다시 큰 문제를 해결할 때 사용

# DP가 적용되기 위한 2가지 조건
# 1) Overlapping Subproblems(겹치는 부분 문제): 동일한 작은 문제들이 반복하여 나타나는 경우에 사용이 가능
# 2) Optimal Substructure(최적 부분 구조): 부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우

# 1) DP로 풀 수 있는 문제인지 확인한다.
# 2) 문제의 변수 파악
# 3) 변수 간 관계식 만들기(점화식)
# 4) 메모하기(memoization or tabulation)
# 5) 기저 상태 파악하기
# 6) 구현하기

s1 = input()
s2 = input()

dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for row in range(1,len(s1)+1):
    for col in range(1,len(s2)+1):
        if s1[row-1] == s2[col-1]:
            dp[row][col] = dp[row-1][col-1]+1
    else:
        dp[row][col] = max(dp[row-1][col],dp[row][col-1])

print(dp[-1][-1])



