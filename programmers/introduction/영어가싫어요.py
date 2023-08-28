def solution(numbers):
    numbers = numbers.replace('zero', '0').replace('one', '1').replace('two', '2').replace('three', '3').replace('four',
                                                                                                                 '4').replace(
        'five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')

    return int(numbers)


# 다른풀이
# enumerate(): 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줌
def solution2(numbers):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for index, num in enumerate(nums):
        numbers = numbers.replace(num, str(index))

    return int(numbers)

# 다른풀이
# 딕셔너리 이용
def solution(numbers):
    alpha2num = {'zero' : 0, 'one':1, 'two':2, 'three' : 3, 'four':4,
                 'five':5,'six' : 6, 'seven' : 7, 'eight':8,'nine':9}
    for k, v in alpha2num.items():
        numbers = numbers.replace(k, str(v))
    return int(numbers)