# 체육대회 (PCCP 모의고사 1회 - 2번)
# https://school.programmers.co.kr/learn/courses/15008/lessons/121684

import itertools

def solution(ability):
    permutations_number = [i for i in range(len(ability))]
    permutations = list(itertools.permutations(permutations_number, r=len(ability[0])))
    
    answer = 0
    for permutation in permutations:
        abilities = [ability[v][i] for i,v in enumerate(permutation)]
        if sum(abilities) >= answer:
            answer = sum(abilities)
            
    return answer