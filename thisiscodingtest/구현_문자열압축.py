# 다시 풀어야함

def solution(s):
    answer = len(s)
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        tmp = s[:i]  # 앞에서부터 i만큼의 문자열 추출
        count = 1

        for j in range(i, len(s), i):
            # tmp와 같다면 압축 가능
            if tmp == s[j:i+j]:
                count += 1
            # 압축 못할 경우
            else:
                if count != 1:
                    b += str(count) + tmp
                else:
                    b += tmp
                tmp = s[j:j+i]  # 초기화
                count = 1
        # 남아있는 문자열 처리
        if count != 1:
            b += str(count) + tmp
        else:
            b += tmp

        answer = min(answer, len(b))
    return answer