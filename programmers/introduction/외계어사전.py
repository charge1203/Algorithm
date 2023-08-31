def solution(spell, dic):
    count = 0
    for i in dic:
        for j in spell:
            if j in i:
                count += 1
        if count == len(spell):
            return 1
        count = 0
    return 2


# 다른풀이
# set을 이용해야했음
def solution2(spell, dic):
    for d in dic:
        if not set(spell) - set(d):
            return 1
    return 2


# 이 문제의 핵심포인트는 dic과 spell 모두 중복된 원소가 없다는 것
# set은 중복허용이 안되니 set을 이용하여 풀어야함
# pell의 알파벳과 dic의 단어를 비교를해서 spell의 알파벳이 들어간 단어를 찾아야함

def solution3(spell, dic):
    spell = set(spell)
    for i in dic:
        if spell.issubset(set(i)):
            return 1
    return 2

# ssubset
# 부분집합인지 아닌지 값을  doolean타입으로 반환해주는 메소드