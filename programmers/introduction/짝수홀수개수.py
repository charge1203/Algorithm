def solution(num_list):
    a=0
    b=0
    for i in num_list:
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    answer = [a,b]
    return answer

def solution2(num_list):
    a = len(list(filter(lambda v: v% 2 ==0, [i for i in num_list])))
    b = len(list(filter(lambda v: v% 2 == 1, [j for j in num_list])))
    answer = [a,b]
    return answer

def solution3(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
