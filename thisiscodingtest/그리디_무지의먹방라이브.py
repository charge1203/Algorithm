# 테스트는 성공했지만 시간초과
# 0초부터 먹기 시작하고, k초에 먹어야할 음식
# k번 먹었음
def solution(food_times, k):
    answer = 0
    t = 0
    while t != k:
        for i in range(len(food_times)):
            if food_times[i] != 0:
                food_times[i] -= 1
                t += 1
                if t == k:
                    answer = (i+1+1)//len(food_times)
            elif sum(food_times) == 0:
                answer = -1
            else:
                continue

    return answer

