# 탑다운
# n = int(input())
# t = []
# p = []
# dp = [0] * (n+1)
# max_value = 0
#
# for _ in range(n):
#     x,y = map(int, input().split())
#     t.append(x)
#     p.append(y)
#
# # 리스트 뒤에서부터 거꾸로 확인
# for i in range(n-1,-1,-1):
#     time = t[i]+i  # 이게 뭐지
#     if time <= n: # 기간 안에 끝나는 경우
#         dp[i] = max(p[i]+dp[time], max_value)
#         max_value = dp[i]
#     else:  # 상담기간 벗어난 경우
#         dp[i] = max_value
#
# print(max_value)


# 보텀업
n = int(input())
sch = [list(map(int, input().split())) for i in range(n)]
# print(sch)

dp = [0] * (n+1)
# print(dp)

for i in range(n):
    for j in range(i+sch[i][0], n+1):
        if dp[j] < dp[i]+sch[i][1]:
            dp[j] = dp[i]+sch[i][1]

print(dp[-1])
