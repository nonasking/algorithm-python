# 2개 이하로 다른 비트
# https://school.programmers.co.kr/learn/courses/30/lessons/77885


# def get_diff(a,b):
#     result = 0
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             result += 1
#         if result > 2:
#             return False
#     return True

# def func(x):
#     y = x + 1
#     bin_x = format(x, 'b')
#     while True:
#         bin_y = format(y, 'b')
#         if len(bin_x) > len(bin_y):
#             bin_y = format(y, 'b').zfill(len(bin_x))
#         elif len(bin_x) < len(bin_y):
#             bin_x = format(x, 'b').zfill(len(bin_y))
#         if get_diff(bin_x,bin_y):
#             return y
#         y += 1

# def solution(numbers):
#     result = [func(number) for number in numbers]
#     return result