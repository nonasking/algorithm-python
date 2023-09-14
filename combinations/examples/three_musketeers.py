# 삼총사(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/131705


from itertools import combinations

def get_combinations(length):
    return list(combinations([i for i in range(length)],3))

def solution(number):
    combinations = get_combinations(len(number))
    
    answer = 0
    
    for combination in combinations:
        sum_values = [number[i] for i in combination]
        if sum(sum_values) == 0:
            answer += 1
    
    return answer