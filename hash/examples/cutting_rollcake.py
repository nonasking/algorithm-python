# 롤케이크 자르기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/132265


def solution(topping):
    result = 0
    first = {i : topping[i] for i in range(len(topping))}    
    first_map = {}
    
    for i in range(len(topping)):
        if topping[i] in first_map:
            first_map[topping[i]] += 1
        else:
            first_map[topping[i]] = 1
    
    second = set()
    
    for i in range(len(topping)):
        second.add(first[i])
        if first_map[first[i]] == 1:
            first_map.pop(first[i])
        else:
            first_map[first[i]] -= 1
        if len(first_map.keys()) == len(second):
            result += 1
        
    return result