import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    data = sys.stdin.readline().split()
    lst.append((data[0], int(data[1])))  # 이렇게 같이 입력받아서 리스트에 저장하는거 생각!

# 딕셔너리 정렬
lst = sorted(lst, key=lambda x:x[1])

for i in lst:
    print(i[0], end=' ')