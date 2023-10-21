import math

def gcd_N(array):
    gcd = array[0]
    for item in array:
        gcd = math.gcd(gcd, item)
    return gcd

def solution(arrayA, arrayB):
    case1, case2 = 0, 0
    a = gcd_N(arrayA)
    b = gcd_N(arrayB)

    # case1
    for b_num in arrayB:
        if b_num % a == 0:
            case1 = 0
            break
        case1 = a

    # case2
    for a_num in arrayA:
        if a_num % b == 0:
            case2 = 0
            break
        case2 = b

    return max(case1, case2)
