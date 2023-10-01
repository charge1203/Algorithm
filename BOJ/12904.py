# 골드5
# 12094

# 백트래킹 이용!!!!!!
# 문제는 s->t로 만들 수 있냐지만, 조건을 거쳐 t->s로 만들 수 있을지!

import sys

s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

if s == t:
    print(1)
else:
    print(0)