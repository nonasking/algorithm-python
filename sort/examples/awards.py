# 명예의 전당
# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    score_sorted = []
    awards = []
    for s in score:
      score_sorted.append(s)
      score_sorted.sort(reverse=True)
      if len(score_sorted) < k:
        awards.append(score_sorted[-1])
      else:
        awards.append(score_sorted[k-1])
    return awards