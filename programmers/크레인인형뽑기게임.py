def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1]) # 스택에 뽑은 인형 넣어주기
                board[j][i-1] = 0  # 뽑은 인형의 자리는 0으로

                if len(stacklist) > 1:  # 인형이 2개 이상일 때
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2  # 뺀 인형 수
                break

    return answer