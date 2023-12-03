# 하샤드 수(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    return True if x % sum(map(int,list(str(x)))) == 0 else False