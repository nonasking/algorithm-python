# 2개 이하로 다른 비트
# https://school.programmers.co.kr/learn/courses/30/lessons/77885


# def get_diff(a,b):
#     if len(a) > len(b):
#         b = '0' * (len(a)-len(b)) + b
#     elif len(a) < len(b):
#         a = '0' * (len(b)-len(a)) + a
#     result = 0
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             result += 1
#         if result > 2:
#             return False
#     return True

# def convert_to_binary(number):
#     return bin(number)[2:]

# def func(x):
#     y = x + 1
#     bin_x = convert_to_binary(x)
#     while True:
#         bin_y = convert_to_binary(y)
#         if get_diff(bin_x,bin_y):
#             return y
#         y += 1

# def solution(numbers):
#     result = [func(number) for number in numbers]
#     return result