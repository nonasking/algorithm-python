# 예상 대진표(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def go_next_round(round, number):
  m, r = divmod(number, 2)
  return round + 1, m+r

def solution(n,a,b):
    rounda, numbera = 0, a
    roundb, numberb = 0, b
    
    while abs(numbera-numberb) != 1 or sum(divmod(numbera,2)) != sum(divmod(numberb,2)):
      rounda, numbera = go_next_round(rounda, numbera)
      roundb, numberb = go_next_round(roundb, numberb)
      
    answer = rounda+1
    return answer