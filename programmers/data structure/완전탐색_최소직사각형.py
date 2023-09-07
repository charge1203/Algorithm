def solution(sizes):
    answer = 0
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    w = sizes[0][0]
    h = sizes[0][1]
    for i in sizes:
        if i[0] > w:
            w = i[0]
        if i[1] > h:
            h = i[1]
    return w*h


# 다른풀이
def solution2(sizes):
    allWidth = []
    allHeight = []
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]

        allWidth.append(size[0])
        allHeight.append(size[1])

    return max(allWidth) * max(allHeight)