# 바탕화면 정리(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/161990


def find_file(location):
    result = []
    for i in range(len(location)):
        if location[i] == '#':
            result.append(i)
    return [min(result), max(result)]

def solution(wallpaper):
    xs = []
    ys = []
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            xs += find_file(wallpaper[i])
            ys.append(i)
            
    return [min(ys), min(xs), max(ys)+1, max(xs)+1]