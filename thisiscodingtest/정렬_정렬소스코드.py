# 선택정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]  # 스와이프

print(array)


# 삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하여 반복
        if array[j] < array[j-1]:  # 인덱스 더 큰게 작은 것보다 값이 작다면 (한 칸씩 왼쪽 이동)
            array[j], array[j-1] = array[j-1], array[j]  # 스와이프
        else:  # 자기보다 작은 데이터를 만나면
            break # 그 위치에서 멈춤

print(array)


# 퀵정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우
        return  # 종료
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right]  # 작은데이터와 피벗 교체
        else:  # 엇갈리지 않았다면
            array[left], array[right] = array[right], array[left]  # 작은데이터와 큰 데이터 교체

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)


# 파이썬 장점을 살린 퀵 정렬
# 얘는 이해감
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array):
    if len(array) <= 1:  #리스트가 하나 이하의 원소만을 담고 있다면
        return array  #종료

    pivot = array[0]  # pivot은 첫번째 원소
    tail = array[1:]  # pivot을 제외한 나머지 리스트

    left_side = [x for x in tail if x<=pivot]  #분할된 왼쪽 부분
    right_side = [x for x in tail if x>pivot]  #분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))


# 계수정렬
#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5 ,9, 0, 3, 1, 6, 2, 9, 1, 4, 8,  0, 5, 2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정보 확인
    for j in range(count[i]):
        print(i, end=' ')