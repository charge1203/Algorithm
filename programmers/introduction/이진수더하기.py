def solution(bin1, bin2):
    num1 = 0
    num2 = 0
    for i in range(len(bin1)):
        num1 += int(bin1[i]) * (2**(len(bin1)-1-i))
    for i in range(len(bin2)):
        num2 += int(bin2[i]) * (2**(len(bin2)-1-i))
    return format(num1+num2, 'b')


# 다른풀이
def solution2(bin1, bin2):
    a1, a2 = (int(bin1,2), int(bin2,2)) # 10진수로 바꾸기
    return format((a1+a2),'b')

def solution3(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer