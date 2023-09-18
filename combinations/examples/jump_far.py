# 멀리 뛰기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

import math


def solution(n):
    
    answer = 0
    
    for i in range(n//2+1):
        answer += math.comb(n-i, i)

    return answer % 1234567