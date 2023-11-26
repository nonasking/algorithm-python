# 콜라츠 추측(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12943


def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (num * 3) + 1

def solution(num):
    count = 0
    
    while count < 500 and num != 1:
        count += 1
        num = collatz(num)
    
    if num == 1:
        return count
    else:
        return -1