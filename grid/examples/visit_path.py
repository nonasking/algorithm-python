# 방문 길이(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/49994


def get_next(before_x, before_y, dir):
    dirs = ['U','D','R','L']
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    index = dirs.index(dir)
    next_x, next_y = before_x + dx[index], before_y + dy[index]
    
    if abs(next_x) > 5 or abs(next_y) > 5:
        return before_x, before_y
    
    return next_x, next_y    

def solution(dirs):
    
    x, y = 0, 0
    
    result = []
    for dir in dirs:
        paths = [str(x)+str(y)]
        x, y = get_next(x,y,dir)
        paths.append(str(x)+str(y))
        paths.sort()
        
        if paths not in result and paths[0] != paths[1]:
            result.append(paths)

    return len(result)