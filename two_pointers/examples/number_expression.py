# 숫자의 표현(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    nums = [i+1 for i in range(n)]
    interval_sum = 0
    end = 0
    count = 0
    for start in range(n):
      while interval_sum < n and end < n:
        interval_sum += nums[end]
        end += 1
      if interval_sum == n:
        count += 1
      interval_sum -= nums[start]
  
    return count