import sys

t = int(sys.stdin.readline())
dice_list = [list(map(int, sys.stdin.readline().split())) for i in range(t)] # 주사위 2차원 배열로 저장
max_sum = 0 # 출력값 초기화

def find_max(dice, bottom): # 탐색할 주사위 배열, 그 주사위의 아랫면에 있어야 할 숫자를 인자로 받음
	for i in range(6):
		if dice[i] == bottom: # 전달받은 주사위 배열을 돌며 아랫면 숫자가 있는 인덱스 판별
			break
	if i == 0: # 아랫면 인덱스가 0일 경우
		return(dice[5], max(dice[1], dice[2], dice[3], dice[4])) # 이 주사위의 윗면이자 다음 주사위의 아랫면은 5번 인덱스가 되며, 나머지 남은 4면 중 가장 큰 값이 해당 주사위의 옆면이 됨
	elif i == 1:
		return (dice[3], max(dice[0], dice[2], dice[4], dice[5]))
	elif i == 2:
		return (dice[4], max(dice[0], dice[1], dice[3], dice[5]))
	elif i == 3:
		return (dice[1], max(dice[0], dice[2], dice[4], dice[5]))
	elif i == 4:
		return (dice[2], max(dice[0], dice[1], dice[3], dice[5]))
	elif i == 5:
		return (dice[0], max(dice[1], dice[2], dice[3], dice[4]))

for i in range(1, 7): # 가장 첫번째 주사위의 1 ~ 6 숫자 중 어떤 숫자를 처음 아랫면으로 놓고 시작했을 때 가장 큰 값이 되는 지 파악하기 위해 for 문 순회
	n_bottom = i # 첫번째 주사위의 아랫면 숫자 결정
	sum = 0 # 매 반복문의 합 초기화
	for j in range(t): # 주사위의 갯수만큼 반복
		n_bottom, ret = find_max(dice_list[j], n_bottom) # 탐색할 주사위, 그리고 그 주사위의 new_bottom을 전달하고, 반환값으로 다음 주사위의 new_bottom과 최대값을 받음
		sum += ret # 탐색한 주사위의 최댓값 합산
	if max_sum < sum: # 첫번째 주사위의 1 ~ 6을 하나씩 아랫면으로 둔 경우의 수마다 최댓값이 큰 경우 갱신
		max_sum = sum
print(max_sum)
