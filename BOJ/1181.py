n = int(input())
word_list = []

for _ in range(n):
    word_list.append(input())

word_list = list(set(word_list))  # 중복 제거
word_list.sort()  # 오름차순 정렬
word_list.sort(key=lambda x: len(x))  # 길이순 정렬

for i in word_list:
    print(i)