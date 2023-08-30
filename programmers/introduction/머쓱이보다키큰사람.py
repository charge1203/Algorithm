def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer


# 다른풀이
def solution2(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

# sort() : 리스트를 정렬하는 함수로, reverse = True로 하게 되면 내림차순으로 정렬이 가능하다. 또한 sort()는 리스트 자체를 변경해버린다. sort()는 리스트의 함수로 리스트만을 받는다.
# sorted() : sort()와 똑같은 기능을 하지만, 단, 리스트 자체를 변경하지 않고 정렬된 리스트를 새로 반환한다. sorted()는 리스트 외에도 다양한 이터러블 객체도 받을 수 있다.
# index() : [찾을 리스트].index(위치를 찾고자 하는 값) / 특정 리스트에서 특정 값이 몇 번째에 위치해 있는지 index 값을 반환해준다.