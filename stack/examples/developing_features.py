# 기능개발(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42586


import math
from collections import deque


def get_deployments(days):
    standard = days[0]
    result = 0
    for i in range(1,len(days)):
        if days[i] <= standard:
            result = i
        else:
            break
    return result
    
def solution(progresses, speeds):
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    
    result = []
    
    while len(days) > 0:
        index = get_deployments(days)
        result.append(index+1)
        del days[:index+1]

    return result