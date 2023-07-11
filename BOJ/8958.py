n = int(input())  #테스트 개수 입력받기

for _ in range(n):  #테스트 개수만큼 반복문 실행
    case = input()  #각 테스트 케이스 문자열 입력
    score = 0
    total = 0
    for j in case:  #각 테스트 케이스의 문자열만큼 반복
        if j == 'O':  #문자열이 'O'일 때
            score += 1
        else:  #문자열이 'X'일 때
            score = 0
        total += score
    print(total)  #각 테스트 케이스에서의 점수 출력