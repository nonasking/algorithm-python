# 올바른 괄호(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    
    result = []
    for value in s:
        result.append(value)
        if result[-2:] == ['(',')']:
            result.pop()
            result.pop()

    return True if result == [] else False