# 크기가 작은 부분 문자열(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/147355


def solution(t, p):
    result = 0
    for i in range(len(t)-(len(p)-1)):
        substr = t[i:i+len(p)]
        if int(substr) <= int(p):
            result += 1
    return result