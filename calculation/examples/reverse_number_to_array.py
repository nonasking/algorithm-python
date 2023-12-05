# 자연수 뒤집어 배열로 만들기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12932


import math


def get_digit(n):
    return int(math.log10(n)) + 1 if n else 0

def solution(n):
    digit = get_digit(n)
    result = []    
    for i in range(digit):
        r = n % (10**(i+1)) // (10**i)
        result.append(r)
    return result