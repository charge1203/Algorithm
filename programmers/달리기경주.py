# 딕셔너리 사용
def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for calling in callings:
        rank = result[calling] # 호명된 선수의 현재 등수
        result[calling] -= 1 # 하나 앞 등수로 바꿔줌 -1
        result[players[rank-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[rank-1], players[rank] = players[rank], players[rank-1] # 위치 변경
    return players


# 일부 시간초과
# swap 방법
def solution2(players, callings):
    answer = []
    for calling in callings:
        rank = players.index(calling)
        players[rank], players[rank-1] = players[rank-1], players[rank]
    return players