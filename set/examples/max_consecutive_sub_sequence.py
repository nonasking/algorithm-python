# 연속 부분 수열 합의 개수(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/131701


def solution(elements):
    sums = set()
    for count in range(len(elements)):
        for i in range(len(elements)):
            start = i
            end = i + count + 1
            if end <= len(elements):
                sums.add(sum(elements[i:i+count+1]))
            else:
                end -= len(elements) 
                sums.add(sum(elements[i:] + elements[:end]))
    return len(sums)