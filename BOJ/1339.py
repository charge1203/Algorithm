n = int(input())

words = []  # 입력단어
dict = {}  # 단어 내의 알파벳별로 수를 저장할 딕셔너리

for _ in range(n):
    words.append(list(input().rstrip()))

for word in words:
    for i in range(len(word)):
        if word[i] not in dict:  # 알파벳이 딕셔너리에 없으면
            dict[word[i]] = 10 ** (len(word) - 1 - i)   # 10^n으로 값 부여하여 저장

        else:  # 딕셔너리에 알파벳이 이미 있으면
            dict[word[i]] += 10 ** (len(word) - 1 - i)  # 자리에 맞게 추가

# dict에 각 알파벳 자리에 맞게 10^n들의 누적이 저장되어 있을 것

dict = sorted(dict.values(), reverse=True)  # 내림차순 정렬 (누적 저장이 큰 알파벳부터 큰 숫자 부여하기 위해)

result = 0
num = 9  # 내림차순 결과에 9부터 배정

for v in dict:
    result += v*num
    num -= 1  # 9부터 하나씩 작게하여 배정

print(result)