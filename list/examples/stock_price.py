# 주식가격(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42584


def find_drop(standard_index, prices):
    result = []
    
    for i in range(standard_index+1, len(prices)):
        if i == (len(prices)-1):
            return (len(prices)-1)-standard_index
        elif prices[i] < prices[standard_index]:
            return i-standard_index
    
    return 0
    

def solution(prices):
    answer = [find_drop(i, prices) for i in range(len(prices))]