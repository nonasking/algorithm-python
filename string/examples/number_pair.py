# 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128


def find_common(X,Y):
    
    result = []
    
    sets = set(X)
    commons = {}
    for s in sets:
        if s in Y:
            commons[s] = min([X.count(s),Y.count(s)])
    
    for i,v in commons.items():
        for _ in range(v):
            result.append(i)
    
    return result

def solution(X, Y):
    common = find_common(X,Y)
    
    if common == []:
        return '-1'
    
    common.sort(reverse=True)
    
    if common[0] == '0':
        return '0'
    
    answer = ''.join(common)
    
    return answer