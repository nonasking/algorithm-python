# 오픈채팅방(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    
    id_nickname_map = {}
    for value in record:
        sliced_words = value.split(' ')
        if sliced_words[0] != 'Leave':
            id_nickname_map[sliced_words[1]] = sliced_words[2]
    
    answer = []
    for value in record:
        sliced_words = value.split(' ')
        if sliced_words[0] == 'Enter':
            answer.append(id_nickname_map[sliced_words[1]] + '님이 들어왔습니다.')
        elif sliced_words[0] == 'Leave':
            answer.append(id_nickname_map[sliced_words[1]] + '님이 나갔습니다.')
            
    return answer