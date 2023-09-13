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