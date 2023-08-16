def solution(rsp):
    dict = {'0':'5','2':'0','5':'2'}
    return ''.join(dict[i] for i in rsp)