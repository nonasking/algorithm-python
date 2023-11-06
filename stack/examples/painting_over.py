# 덧칠하기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/161989#


def solution(n, m, section):
    result = 0
    i = 0
    while len(section) > 0:
        start = section.pop(0)
        while i < len(section):
            if section[i] < start + m:
                section.pop(i)
                i -= 1
            else:
                break
            i += 1
        result += 1
    return result