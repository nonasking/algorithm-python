# 완주하지 못한 선수(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    if (set(participant) - set(completion)):
        return (set(participant) - set(completion)).pop()
    for value in completion:
        if participant.count(value) > completion.count(value):
            return value