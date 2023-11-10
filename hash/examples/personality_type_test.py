# 성격 유형 검사(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/118666


def solution(survey, choices):
    characters = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    
    for i in range(len(survey)):
        for character in characters.keys():
            if character.find(survey[i][0]) != -1:
                index = character.find(survey[i][1]) # 0 1
                characters[character] += (choices[i]-4) if index == 0 else -1 * (choices[i]-4)
                break
    
    result = ''
    for character in characters.keys():
        if characters[character] > 0:
            result += character[0]
        elif characters[character] < 0:
            result += character[1]
        else:
            result += min(character[0], character[1])
    
    return result