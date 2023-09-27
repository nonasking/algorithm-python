# 타겟 넘버(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/43165


from itertools import product


def solution(numbers, target):
    
    signs = list(product([-1,1], repeat=len(numbers)))
    answer = 0
    for sign in signs:
        value = 0
        for i in range(len(numbers)):
            value += (sign[i] * numbers[i])
        if value == target:
            answer += 1
    
    return answer