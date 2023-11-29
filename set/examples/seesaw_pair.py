# 시소 짝꿍(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/152996


# def check_equilibrium(a,b):
#     distances = [2,3,4]
#     a_weights = set([a*distance for distance in distances])
#     for distance in distances:
#         if b*distance in a_weights:
#             return True
#     return False

# def solution(weights):
#     result = 0
#     for i in range(len(weights)-1):
#         for j in range(1,len(weights)):
#             if i < j and check_equilibrium(weights[i],weights[j]):
#                 result += 1
#     return result