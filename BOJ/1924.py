# 구현
import sys

x,y = map(int, sys.stdin.readline().split())
day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', "SAT"]
day = 0

if x == 1:
    day = y
elif x == 2:
    day = 31+y
elif x == 3:
    day = 31+28+y
elif x == 4:
    day = 31+28+31+y
elif x == 5:
    day = 31+28+31+30+y
elif x == 6:
    day = 31+28+31+30+31+y
elif x == 7:
    day = 31+28+31+30+31+30+y
elif x == 8:
    day = 31+28+31+30+31+30+31+y
elif x == 9:
    day = 31+28+31+30+31+30+31+31+y
elif x == 10:
    day = 31+28+31+30+31+30+31+31+30+y
elif x == 11:
    day = 31+28+31+30+31+30+31+31+30+31+y
elif x == 12:
    day = 31+28+31+30+31+30+31+31+30+31+30+y

print(day_list[day%7])


# 깔끔하고 간결한 코드는 없을까
day = 0
month = [31,28,31,30,31,30,31,31,30,31,30,31]
day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', "SAT"]
x,y = map(int, sys.stdin.readline().split())

for i in range(x-1):
    day += month[i]

print(day_list[(day+y)%7])
