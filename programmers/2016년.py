def solution(a, b):
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return days[(sum(months[:a - 1]) + b) % 7]


# 틀린 솔루션
# 굳이 이렇게 할 필요도 없고 요일도 굳이 저렇게 고집할 필요가 없음
def solution2(a, b):
    answer = ''
    weekofdays = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    days = 0
    days_per_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        days += days_per_month[i]
    days += b-1
    print(days)
    print(days%7)
    if (5 + days%7) > 7:
        answer = weekofdays[days%5-2]
    else:
        answer = weekofdays[days%5]
    return answer