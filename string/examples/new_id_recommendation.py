# 신규 아이디 추천(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):

    # 1
    new_id = new_id.lower()
    
    # 2
    new_value = ''
    for letter in new_id:
        if letter.isalnum() or letter in ['-','_','.']:
            new_value += letter
    new_id = new_value
    
    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')
        
    # 5
    if new_id == '':
        new_id = 'a'
    
    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')
        
    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id