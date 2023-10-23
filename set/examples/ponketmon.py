# 폰켓몬(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums):
    return len(nums)//2 if len(nums)//2 < len(set(nums)) else len(set(nums))