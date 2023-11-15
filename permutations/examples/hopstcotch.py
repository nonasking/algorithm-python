# 땅따먹기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12913


import itertools


def solution(land):
    
    orders = [''.join(v) for v in itertools.product(['0','1','2','3'], repeat=len(land))]
    
    orders = [v for v in orders if '00' not in v and '11' not in v and '22' not in v and '33' not in v]
    
    result = 0
    for order in orders:
        sum_value = sum([land[i][int(order[i])] for i in range(len(order))])
        if result <= sum_value:
            result = sum_value

    return result