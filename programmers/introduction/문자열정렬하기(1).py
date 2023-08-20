# 숫자 추출은 시중 코드 이용
# int로 변환, 리스트로 변환
# 정렬 따로

import re
def solution(my_string):
    answer = list(map(int,re.sub(r'[^0-9]', '', my_string)))
    answer.sort()
    return answer


# 다른 풀이
# try except를 사용해 i가 int로 형변환이 가능하면 answer에 추가시키고 불가능하면 continue
def solution2(my_string):
    answer = []
    for i in my_string:
        try:
            answer.append(int(i))
        except:
            continue
    answer.sort()
    return answer


# 다른풀이
def solution3(my_string):
    return sorted([int(i) for i in str(my_string) if i.isdigit()])


import re
def solution4(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

def solution5(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))