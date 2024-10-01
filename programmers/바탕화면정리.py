# 내 코드
# #이 있는 자리의 리스트를 정리하고, x자리 최소, y자리 최소, x자리 최대 + 1, y자리 최대 + 1
def solution(wallpaper):
    answer = []
    sharp = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                sharp.append([i, j])
    answer.append(min(sharp, key=lambda x: x[0])[0])
    answer.append(min(sharp, key=lambda x: x[1])[1])
    answer.append(max(sharp, key=lambda x: x[0])[0] + 1)
    answer.append(max(sharp, key=lambda x: x[1])[1] + 1)

    return answer


def solution1(wallpaper):
    x, y = [], []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)

    return [min(x), min(y), max(x) + 1, max(y) + 1]  # 결과가 더 간단하네
# 그치 굳이 리스트의 쌍을 지어서 만들 필요는 없지..