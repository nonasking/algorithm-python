# [PCCE 기출문제] 10번 / 데이터 분석
# https://school.programmers.co.kr/learn/courses/30/lessons/250121


def check_data(data, criteria_index, val_ext):
    return True if data[criteria_index] < val_ext else False

def solution(data, ext, val_ext, sort_by):
    criteria = {'code':0, 'date': 1, 'maximum':2, 'remain':3}
    result = sorted([value for value in data if check_data(value, criteria[ext], val_ext)], key=lambda x : x[criteria[sort_by]])    
    return result