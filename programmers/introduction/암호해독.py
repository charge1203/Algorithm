# 그냥 range 바꿔주니 런타임 에러 해결
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer

# 런타임에러 코드
def solution2(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher)+1, code):
        answer += cipher[i]
    return answer