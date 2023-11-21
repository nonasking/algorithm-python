# 공원 산책(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def get_next_location(x,y,route,park):
  directions = ['N','S','W','E']
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  input_x, input_y = x,y
  direction, count = route.split(' ')
  index = directions.index(direction)
  for i in range(int(count)):
    if -1 < x + dx[index] < len(park) and -1 < y + dy[index] < len(park[0]):
      x = x + dx[index]
      y = y + dy[index]
      if park[x][y] == 'X':
        return input_x, input_y
    else:
      return input_x, input_y

  return x,y

def solution(park, routes):
    x, y = 0, 0
    for i in range(len(park)):
      for j in range(len(park[0])):
        if park[i][j] == 'S':
          x,y = i,j
    for route in routes:
      x,y = get_next_location(x,y,route,park)
    answer = [x,y]
    return answer