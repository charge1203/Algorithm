n = int(input())
word_list = []
count = n

for _ in range(n):
    word_list.append(input())

for i in range(len(word_list)):
    for j in range(0, len(word_list[i])-1):  # 인덱스 주의
        if word_list[i][j] == word_list[i][j+1]:
            pass
        elif word_list[i][j] in word_list[i][j + 1:]:
            count -= 1
            break

print(count)