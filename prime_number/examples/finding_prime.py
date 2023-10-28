# 소수 찾기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42839


import math
from itertools import permutations


def check_prime(number):
    if number < 2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    result = 0
    values = set()
    for i in range(1,len(numbers)+1):
        values = values | set(int(''.join(number)) for number in list(permutations(numbers, i)))
    for value in values:
        if check_prime(value):
            result += 1
    return result