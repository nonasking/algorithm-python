# 소수 찾기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12921


import math


def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(n):
    return sum([1 if is_prime_number(i) else 0 for i in range(2,n+1)])