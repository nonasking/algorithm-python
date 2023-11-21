# 행렬의 덧셈(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12950


def solution(arr1, arr2):
    
    answer = []
    for y in range(len(arr1)):
        answer.append([])
        for x in range(len(arr1[0])):
            answer[y].append(arr1[y][x] + arr2[y][x])
            
    return answer