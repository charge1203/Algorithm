# 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if array[mid] == target: # 찾은 경우
        return mid  # 중간점 인덱스 반환
    elif array[mid] > target:  # 찾고자하는 값이 중간값보다 작다면
        return binary_search(array, target, start, mid-1)  # 왼쪽 확인
    else:  # 찾고자하는 값이 중간값보다 크다면
        return binary_search(array, target, mid+1, end)  # 오른쪽 확인

n, target = list(map(int, input().split()))  # 원소 개수, 찾고자하는 값 인ㅂ력받기
array = list(map(int, input().split()))  # 전체 리스트

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)


# 반복문 이용
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:  # target이 중간값보다 작다면
            end = mid-1  # end 조정하여 왼쪽 탐색
        else:  # target이 중간값보다 크다면
            start = mid+1  # start 조정하여 오른쪽 탐색
    return None

n, target = list(map(int, input().split()))  # 원소 개수, 찾고자하는 값 인ㅂ력받기
array = list(map(int, input().split()))  # 전체 리스트

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)