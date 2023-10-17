# JadenCase 문자열 만들기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12951


def solution(s):
    s = s.replace(' ', '~')
    strs = []
    for substr in s.split('~'):
        if substr != '':
            substr = substr[0].upper() + substr[1:].lower()
        strs.append(substr)
    result = '~'.join(strs)
    result = result.replace('~', ' ')
    return result