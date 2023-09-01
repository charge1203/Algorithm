# 잘 못품 다시 풀어야함
def solution(numlist, n):
    numlist = sorted(numlist, reverse = True)
    numlist = sorted(numlist, key = lambda x : abs(n-x))
    return numlist

# 다른풀이
# lambda 함수 공부하기
def solution2(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer