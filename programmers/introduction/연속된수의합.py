# 어케할지 모르겠어서 그냥 무작정 함
def solution(num, total):
    answer = []
    center = total//num
    if num %2 !=0:
        answer.append(center)
        for i in range(1, (num-1)//2+1):
            answer.append(center-i)
        for i in range(1, (num-1)//2+1):
            answer.append(center+i)
    else:
        answer.append(center)
        for i in range(1, (num-1)//2+1):
            answer.append(center-i)
        for i in range(1, (num-1)//2+2):
            answer.append(center+i)
    return sorted(answer)

# 얘가 제일 와닿음
def solution4(num, total):
    avg = total // num
    return [i for i in range(avg - (num-1)//2, avg + (num+2)//2)]

# 다른풀이
def solution2(num, total):
    d=0
    for i in range(1, num):
        d += i
    start=(total-d)//num  # 이게 잘 이해가 안가긴 함
    answer = [i for i in range(start, start+num)]
    return answer


def solution3(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start_num = diff//num
    answer = [i+1+start_num for i in range(num)]
    return answer