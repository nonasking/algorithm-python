# 뒤에 있는 큰 수 찾기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

# def find_bigger(i, numbers):
#     if i == len(numbers):
#         return -1
#     for j in range(i+1, len(numbers)):
#         if numbers[j] > numbers[i]:
#             return numbers[j]
#     return -1

# def solution(numbers):
#     return [find_bigger(i, numbers) for i in range(len(numbers))]