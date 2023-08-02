def solution(nums):
    answer = len(set(nums))  # 중복 제거, 입력 받은 폰켓몬 종류 수

    if answer > len(nums) / 2:  # 폰켓몬 종류 수가 폰켓몬 총 수의 절반보다 많다면
        return len(nums) / 2  # 원래 절반만 가져가기로 했으니
    else:
        return answer