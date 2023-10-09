# n^2 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/87390


def solution(n, left, right):
    
    result = []
    
    for i in range(left, right+1):
        x = (i // n) + 1
        y = (i % n) + 1
        result.append(max(x,y))
    
    return result