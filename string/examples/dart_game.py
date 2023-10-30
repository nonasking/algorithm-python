# 다트 게임(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/17682


def slice_dart_result(dartResult):
    result = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            result.append(i)
    
    i = 1
    while True:
        if result[i] == result[i-1] + 1:
            result.pop(i)
        i += 1
        if i > len(result) - 1:
            break
    
    return [dartResult[:result[1]], dartResult[result[1]:result[2]], dartResult[result[2]:]]

def separate_single_result(single_result):
    result = {}
    for value in single_result:
        if value.isdigit():
            if 'score' in result:
                result['score'] += value
            else:
                result['score'] = value
        elif value.isalpha():
            result['bonus'] = value
        else:
            result['option'] = value
    result['score'] = int(result['score'])    
    return result
    
def solution(dartResult):
    sliced_results = slice_dart_result(dartResult)
    
    bonuss = ['S','D','T']
    
    result = [0] * 3
    for i in range(len(sliced_results)):
        separated_single_result = separate_single_result(sliced_results[i])
        score = separated_single_result['score'] ** (bonuss.index(separated_single_result['bonus']) + 1)
        if 'option' in separated_single_result:
            if separated_single_result['option'] == '#':
                score *= -1
            if separated_single_result['option'] == '*':
                if i > 0:
                    result[i-1] = result[i-1] * 2
                score *= 2
        result[i] = score

    return sum(result)