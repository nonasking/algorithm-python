x, y = 1, 1 # 입력값 받음

dx = [2, -2, 2, -2, -1, 1, 1, -1]
dy = [-1, 1, 1, -1, 2, -2, 2, -2]


paths = []

for i in range(8):

  if 0 < x + dx[i] < 9 and 0 < y + dy[i] < 9:
    moved_x = x + dx[i]
    moved_y = y + dy[i]
    paths.append((moved_x,moved_y))

  
print(len(set(paths)))