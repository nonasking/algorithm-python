# 더 맵게(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
  heapq.heapify(scoville)
  answer = 0

  while scoville[0] < K:
    if len(scoville) < 2:
      return -1
    mixed = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
    heapq.heappush(scoville, mixed)
    answer += 1

  return answer