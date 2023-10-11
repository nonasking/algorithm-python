# 이진 변환 반복하기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/70129


def convert_number(s):
    return format(s.count('1'), '#b')[2:]

def solution(s):
    result = [0,0]
    
    while s != '1':
        result[0] += 1
        result[1] += s.count('0')
        s = convert_number(s)
    
    return result