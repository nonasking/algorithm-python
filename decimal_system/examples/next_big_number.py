# 다음 큰 숫자(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12911


def is_next_big_number(n,m):
    if format(m,'b').count('1') == format(n,'b').count('1'):
        return True
    return False

def solution(n):
    m = n + 1
    while True:
        if is_next_big_number(n, m):
            return m
        m += 1