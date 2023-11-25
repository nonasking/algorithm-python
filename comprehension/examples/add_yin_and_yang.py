# 음양 더하기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/76501


def solution(absolutes, signs):
    
    result = 0
    
    for i in range(len(absolutes)):
        result += absolutes[i] if signs[i] else absolutes[i] * -1
    
    return result