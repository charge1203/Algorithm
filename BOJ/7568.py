n = int(input())

data = []  # 몸무게, 키 저장
rank = []  # 등수정보를 저장
for i in range(n):
    a, b = map(int, input().split())  # 몸무게, 키 입력 받음
    data.append((a, b))  # 몸무게와 키를 묶어서 list에 append 해줌

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:  # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1
    rank.append(count + 1)  # 덩치 등수는 자신보다 몸무게 키 모두 큰 사람의 수 + 1 이므로 count + 1을 저장

for d in rank:
    print(d, end=" ")
