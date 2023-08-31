def solution(sides):
    answer = 0
    for i in range(1, sum(sides)):
        tri = sides.copy()
        tri.append(i)
        if max(tri) < sum(tri)-max(tri):
            answer+=1
    return answer

# 다른풀이
# 아직도 이해가 안감
def solution2(sides):
    return sum(sides) - (max(sides) - min(sides)) -1
