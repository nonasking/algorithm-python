# 옹알이(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/133499


def check_babbling(babbling):
    pronuns = ["aya", "ye", "woo", "ma"]
    
    for pronun in pronuns:
        if pronun + pronun in babbling:
            return False
    
    for pronun in pronuns:
        babbling = babbling.replace(pronun, '/')

    babbling = babbling.replace('/', '')
        
    if len(babbling) > 0:
        return False
    
    return True

def solution(babbling):
    answer = 0
    
    for babble in babbling:
        if check_babbling(babble):
            answer += 1
    
    return answer