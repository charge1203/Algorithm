n = int(input())
dict = {}

# 책 이름: key, 팔린 개수: value

for _ in range(n):  # 책 제목, count에 대한 딕셔너리 생성
    book = input()
    if book not in dict:
        dict[book] = 1
    else:
        dict[book] += 1

max_value = max(dict.values())  # 딕셔너리에서 value가 최대인 값 저장

best = []
for key, value in dict.items():
    if value == max_value:
        best.append(key)  # 최대 카운트인 책 제목만 있는 리스트 만들기

print(sorted(best)[0])  # 사전식으로 제일 먼저인 것 출력

