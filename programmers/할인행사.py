from collections import Counter


def solution(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n

    for i in range(len(discount) - 9):
        c = Counter(discount[i:i + 10])
        if c == check:
            answer += 1

    return answer


def solution2(want, number, discount):
    answer = 0
    dict_wishlist = {}

    for i in range(len(want)):
        dict_wishlist[want[i]] = number[i]

    for i in range(len(discount) - 9):
        dict_tmp = dict_wishlist.copy()
        for j in range(i, i + 10):
            if discount[j] in dict_tmp and dict_tmp[discount[j]] != 0:
                dict_tmp[discount[j]] -= 1
            else:
                break
        if sum(dict_tmp.values()) == 0:
            answer += 1

    return answer


def solution3(want, number, discount):
    answer = 0
    list_all_want = []

    for i in range(len(want)):
        for j in range(number[i]):
            list_all_want.append(want[i])
    list_all_want.sort()

    for i in range(len(discount) - 9):
        list_10 = discount[i: i + 10]
        list_10.sort()
        if list_all_want == list_10:
            answer += 1

    return answer