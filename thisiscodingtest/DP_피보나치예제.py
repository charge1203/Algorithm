# 피보나치 함수를 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))


# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

#피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo2(x):
    if x == 1 or x == 2:  #종료 조건 (1 또는 2일 때 1 반환)
        return 1
    if d[x] != 0:  #이미 계산한 적 있는 문제라면
        return d[x]  #그대로 반환

    #아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo2(99))


# 보텀업
# 앞서 계산된 결과 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])