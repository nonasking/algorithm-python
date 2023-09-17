# 점프와 순간이동(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12980


def solution(n):
    k = 0
    
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            k += 1
    
    ans = k
    return ans