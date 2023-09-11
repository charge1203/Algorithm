# 인덱스가 아닌 거리를!!
n,c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

start = 1  # 가능한 최소 거리
end = house[-1]-house[0]  # 가능한 최대 거리
result = 0

while(start<=end):
    mid = (start+end)//2
    value = house[0]
    count = 1
    # 현재의 mid 값 이용해 공유기 설치
    for i in range(1,n):
        if house[i] >= value+mid:
            value = house[i]
            count += 1
    if count >= c:  # c개 이상 공유기를 설치할 수 있는 경우, 거리 증가
        start = mid+1
        result = mid  # 최적의 결과 저장
    else:  # c개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        end = mid-1

print(result)