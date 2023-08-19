def solution(n):
    num = []
    answer = 0

    for i in range(2, n + 1):  # 2부터 세기
        for j in range(1, i + 1):  # 약수 찾기
            if i % j == 0:
                num.append(i)  # j로 나눠 떨어지는 i 개수를 세기 위함

        # 2부터 약수의 개수만큼 해당 수(i)가 num 리스트에 저장될 것
        if num.count(i) >= 3:  # 약수가 세개 이상일 때
            answer += 1  # 합성수 카운트 증가

    return answer


# 다른 풀이
def solution2(n):
    output = 0
    for i in range(4, n + 1):  # 합성수는 4부터 있으니까?
        for j in range(2, int(i ** 0.5) + 1): # 니눠 떨어지는 n 이하의 모든 수를 보지 않아도 됨
            if i % j == 0:  # j 범위의 수 중 하나라도 나눠 떨어진다면 합성수일테니
                output += 1
                break
    return output


# 다른풀이2
def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))

def solution3(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))