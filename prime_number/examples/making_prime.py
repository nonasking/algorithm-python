# 소수 만들기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12977


import math
from itertools import combinations


def check_prime_number(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    numbers = list(sum(pair) for pair in list(combinations(nums, 3)))
    result = sum([1 for number in numbers if check_prime_number(number)])
    
    return result