# 연속된 부분 수열의 합(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/178870


def solution(sequence, k):
    answer = []
    start = 0
    end = 0
    
    while True:
        answer.append(sequence[end])
        while sum(answer) > k:
            start += 1
            answer.pop(0)
        if sum(answer) == k:
            return answer
        end += 1

    return answer