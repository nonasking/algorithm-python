# 피보나치 수(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    
    d = [0,1] + [0] * (n-1)
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
        
    return d[n] % 1234567