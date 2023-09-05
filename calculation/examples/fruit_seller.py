# 과일 장수(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    score.sort(reverse=True)
    boxes_count = len(score) // m
    apples_count = boxes_count * m
    score = score[:apples_count]
    answer = 0
    for i in range(len(score)):
      if (i+1) % m == 0:
        answer += score[i] * m 
    return answer