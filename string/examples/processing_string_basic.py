# 문자열 다루기 기본 (프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12918


def solution(s):
    return s.isdigit() and len(s) in [4,6]