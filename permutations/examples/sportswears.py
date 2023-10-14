# 체육복(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42862#


from itertools import product


def solution(n, lost, reserve):
    filtered_reserve = [student for student in reserve if student not in lost]
    filtered_lost = [student for student in lost if student not in reserve]
    signs = list(product([1,-1],repeat=len(filtered_reserve)))
    
    cases = []
    rent = 0
    for sign in signs:
        case = set([sign[i] + filtered_reserve[i] for i in range(len(filtered_reserve))])
        if 0 not in case and case not in cases:
            common = len(set(filtered_lost) & case)
            cases.append(case)
            if rent <= common:
                rent = common
    
    return n - (len(filtered_lost) - rent)
