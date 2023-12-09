# 점 찍기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/140107


# import math


# def solution(k, d):
#     dots = set()
#     for a in range(d+1):
#         for b in range(d+1):
#             if math.sqrt((a*k)**2 + (b*k)**2) <= d:
#                 dots.add((a*k, b*k))
#     return len(dots)