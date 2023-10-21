def solution(s, skip, index):
    answer = ""

    alpha = "abcdefghijklmnopqrstuvwxyz"  # 알파벳

    for ch in skip:  # ch => skip의 문자 하나하나
        if ch in alpha:
            alpha = alpha.replace(ch, "")  # 알파벳 안에 skip 문자들 제거

    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]  # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change

    return answer



# 몇 개 런타임 에러...
from string import ascii_lowercase

def solution2(s, skip, index):
    answer = ''
    alpha_list = list(ascii_lowercase)
    for i in list(skip):
        alpha_list.remove(i)
    loca = {a: alpha_list.index(a) for a in s}
    for i in range(len(s)):
        new_idx = loca[s[i]] + index
        if new_idx > len(alpha_list) - 1:
            new_idx -= len(alpha_list)
        answer += alpha_list[new_idx]
    return answer