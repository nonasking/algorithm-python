# 의상(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def get_clothes(clothes):
  clothes_map = {}
  for cloth in clothes:
    if cloth[1] in clothes_map:
      clothes_map[cloth[1]].append(cloth[0])
    else:
      clothes_map[cloth[1]] = [cloth[0]]
  return list(clothes_map.values())

def solution(clothes):
    clothes = get_clothes(clothes)
    answer = 1
    for cloth in clothes:
      answer *= (len(cloth)+1)
    answer -= 1
    return answer