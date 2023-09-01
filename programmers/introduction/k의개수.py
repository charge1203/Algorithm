# 자칫하다 시간초과 뜰 것처럼 생긴 코드임
def solution(i, j, k):
    answer = 0
    for a in range(i,j+1):
        for b in str(a):
            if str(k)==b:
                answer += 1
    return answer

# 두번째 try
# 그나마 시간 덜 걸릴듯 함
def solution2(i, j, k):
    answer = 0
    for a in range(i,j+1):
        if str(k) in str(a):
            answer += str(a).count(str(k))
    return answer