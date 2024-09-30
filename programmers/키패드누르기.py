kp = {
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2],
    "*": [3, 0], 0: [3, 1], "#": [3, 2]
}


# 키패드 위치를 딕셔너리에 저장

def dist(point1, point2):  # 거리 재는 함수를 만듦
    y1, x1 = point1
    y2, x2 = point2
    return abs(y2 - y1) + abs(x2 - x1)  # 거리구하기 공식


def solution(numbers, hand):
    result = ''
    lh = kp['*']
    rh = kp['#']

    for num in numbers:
        if num in [1, 4, 7]:
            lh = kp[num]
            result += 'L'
        elif num in [3, 6, 9]:
            rh = kp[num]
            result += 'R'
        else:
            if dist(lh, kp[num]) > dist(rh, kp[num]):
                rh = kp[num]
                result += 'R'
            elif dist(lh, kp[num]) < dist(rh, kp[num]):
                lh = kp[num]
                result += 'L'
            else:
                if hand == 'right':
                    rh = kp[num]
                    result += 'R'
                else:
                    lh = kp[num]
                    result += 'L'
    return result