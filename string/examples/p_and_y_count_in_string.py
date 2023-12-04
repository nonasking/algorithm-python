# 문자열 내 p와 y의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/12916


def solution(s):
    s = s.lower()
    p_cnt = 0
    y_cnt = 0
    for value in s:
        if value == 'p':
            p_cnt += 1
        elif value == 'y':
            y_cnt += 1
    return True if p_cnt == y_cnt else False