def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

# 다른풀이
def solution1(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]

# 이 풀이를 내 풀이와 비슷하게 바꾼거
def solution2(num_list, n):
    return [num_list[ix:ix+n] for ix in range(0, len(num_list), n)]

# numpy 이용한 다른 풀이
import numpy as np
def solution3(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()