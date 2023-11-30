# 정수 제곱근 판별(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12934


import math


def solution(n):
    root = math.sqrt(n)
    return (root+1) ** 2 if root.is_integer() else -1