import sys

n = int(sys.stdin.readline())
n = str(n)
a = len(n)//2
b = 0
c = 0
for i in n[0:a]:
    b += int(i)
for i in n[a:]:
    c += int(i)

if b == c:
    print('LUCKY')
else:
    print('READY')