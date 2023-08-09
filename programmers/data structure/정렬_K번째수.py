def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        a = array[(commands[i][0]-1):commands[i][1]]
        a.sort()
        answer.append(a[commands[i][2] - 1])

    return answer


def solution2(array, commands):
    answer = []

    for i in commands:
        ary = array[i[0] - 1: i[1]]  # 문제에서 주어진 크기만큼 자르기
        ary.sort()  # sort 함수로 정렬
        answer.append(ary[i[2] - 1])  # k 번째 값 집어넣기

    return answer