i = 1
while True:
    # 연속하는 p일 중 l일 동안만 사용 가능. v일 간의 휴가
    l, p, v = map(int, input().split())
    if l+p+v == 0:
        break

    result = (v//p) * l + min(v%p, l)  # 나머지보다 사용 가능한 l이 더 클 수도
    print('Case %d: %d' %(i, result))
    i += 1