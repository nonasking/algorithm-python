# 롤케이크 자르기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/132265


def solution(topping):
    result = 0
    
    first = {top: topping.count(top) for top in topping}
    
    second = set()
    for top in reversed(topping):
        second.add(top)
        if first[top] > 1:
            first[top] -= 1
        else:
            del first[top]
        if len(first) == len(second):
            result += 1
        
    return result