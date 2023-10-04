# 튜플(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/64065


def solution(s):
    s = s[2:-2] .split('},{')
    s.sort(key=len)
    
    result = []
    for value in s:
        numbers = value.split(',')
        for number in numbers:
            if int(number) not in result:
                result.append(int(number))
    
    return result