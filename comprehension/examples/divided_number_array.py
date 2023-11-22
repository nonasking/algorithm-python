# 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    result = sorted([number for number in arr if number % divisor == 0])
    return result if len(result) > 0 else [-1] 