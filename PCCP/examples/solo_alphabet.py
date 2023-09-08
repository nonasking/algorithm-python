# 외톨이 알파벳 (PCCP 모의고사 1회 - 1번)
# https://school.programmers.co.kr/learn/courses/15008/lessons/121683

def check_solo(index, value, input_string):
    if value in input_string[:index] and input_string[index-1] != value:
        return True
    return False

def solution(input_string):
    answer = []
    for i in range(len(input_string)):
        if check_solo(i, input_string[i], input_string):
            answer.append(input_string[i])
    if answer == []:
        return 'N'
    answer = list(set(answer))
    answer.sort()
    return ''.join(answer)