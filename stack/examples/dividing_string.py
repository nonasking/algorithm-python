# 문자열 나누기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/140108


def cut_string(string):
    key = string[0]
    key_count = 0
    not_key_count = 0
    for i in range(len(string)):
        if key == string[i]:
            key_count += 1
        else:
            not_key_count += 1
        if key_count == not_key_count:
            return string[i+1:]
    return -1

def solution(s):
    result = 0

    while len(s) > 0 and cut_string(s) != -1:
        s = cut_string(s)
        result += 1
    
    if len(s) > 0:
        result += 1
        
    return result