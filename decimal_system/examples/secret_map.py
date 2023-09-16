# 비밀 지도(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/17681


def convert_number(number, n):
    result = bin(number)[2:]
    if len(result) < n:
        for _ in range(n-len(result)):
            result = '0' + result
    return result

def solution(n, arr1, arr2):
    bin1 = [convert_number(number, n) for number in arr1]
    bin2 = [convert_number(number, n) for number in arr2]
    maps = []
    for i in range(n):
        value = ''
        for j in range(n):
            if int(bin1[i][j]) + int(bin2[i][j]) == 0:
                value += ' '
            else:
                value += '#'
        maps.append(value)
    answer = maps
    
    return answer