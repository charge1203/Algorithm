def solution1(participant, completion):
    # 둘 다 정렬
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if (participant[i] != completion[i]):  # 정렬했는데 다르다면
            return participant[i]  # 걔가 완주하지 못한 애

    # completion 길이 내에서 두 리스트가 다 같다면
    return participant[len(participant) - 1]  # participant 리스트에서 마지막이 완주 못한 애


# Counter 이용
# counter: 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻을 수 있음
from collections import Counter

def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)

    return list(answer.keys())[0]
