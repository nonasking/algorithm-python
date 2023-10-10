# 행렬의 곱셈(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12949


def get_multiple(arr1, arr2, a, b):
    row = arr1[a]
    column = [arr2[x][b] for x in range(len(arr2))]
    
    result = 0
    
    for i in range(len(row)):
        result += row[i] * column[i]
    
    return result

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    for y in range(len(arr1)):
        for x in range(len(arr2[0])):
            answer[y][x] = get_multiple(arr1, arr2, y, x)
            
    return answer