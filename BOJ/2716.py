import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    op = sys.stdin.readline()

    maxDepth = 0
    tree = list()
    for o in op:
        if o == ']':
            maxDepth = max(len(tree), maxDepth)
            tree.pop()
        else:
            tree.append('[')

    print(2**maxDepth)