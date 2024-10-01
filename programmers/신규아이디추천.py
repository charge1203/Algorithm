# 지저분한 나의 코드.....
import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    # 정규표현식
    new_id = re.sub(r'[^a-z0-9._-]', '', new_id)
    new_id = re.sub(r'\.{2,}', '.', new_id)
    new_id = new_id.strip('.')
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id.rstrip('.')
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id



# # 3단계 ..., ..을 .으로 치환
#     while '..' in new_id:
#         new_id = new_id.replace('..', '.')