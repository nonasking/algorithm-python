# 키패드 누르기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/67256


def get_distance(before, after):
    keypads = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    
    before_x, before_y = 0,0
    after_x, after_y = 0,0
    
    for y in range(len(keypads)):
        for x in range(len(keypads[0])):
            if keypads[y][x] == before:
                before_x, before_y = x,y
            if keypads[y][x] == after:
                after_x, after_y = x,y

    return abs(before_x-after_x) + abs(before_y-after_y)

def solution(numbers, hand):
    
    fingers = {'L':'*', 'R':'#'}
    
    answer = ''
    
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer += 'L'
            fingers['L'] = numbers[i]
        elif numbers[i] in [3,6,9]:
            answer += 'R'
            fingers['R'] = numbers[i]
        else:
            L_distance = get_distance(fingers['L'], numbers[i])
            R_distance = get_distance(fingers['R'], numbers[i])
            if L_distance < R_distance:
                answer += 'L'
                fingers['L'] = numbers[i]
            elif L_distance > R_distance:
                answer += 'R'
                fingers['R'] = numbers[i]
            else:
                answer += hand[0].upper()
                fingers[hand[0].upper()] = numbers[i]
    
    return answer