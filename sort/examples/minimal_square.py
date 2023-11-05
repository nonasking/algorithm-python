# 최소직사각형(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    sorted_sizes = [sorted(size) for size in sizes]
    maximal_width = 0
    maximal_height = 0
    for size in sorted_sizes:
        if size[0] > maximal_width:
            maximal_width = size[0]
        if size[1] > maximal_height:
            maximal_height = size[1]
    return maximal_width * maximal_height