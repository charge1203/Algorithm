def solution(numbers):
    #0. key point
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda num: num*3, reverse=True) #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교

    # join한 값을 int로 만들어 준 후 원하는 return값이 str이기 때문에 다시 str로 변환한다.
    return str(int(''.join(numbers)))
