import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
result = 0 # 총 그룹 수
count = 0  # 현재 그룹에 포함된 모험가 수

a.sort()
# 큰 공포도를 가진 사람부터 묶는다 생각했는데
# 사람을 놓고 가도 되니 작은 애부터 묶기

for i in a:
    count += 1  # 현재 그룹에 해당 모험가 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 그룹 결성했으니까
        count = 0  # 그룹에 있던 모험가 수 초기화

print(result)