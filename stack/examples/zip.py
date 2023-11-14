# 압축(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/17684


from string import ascii_uppercase


def update_dictionary(dictionary, msg):
    w = msg
    w_stack = list(w)
    
    if w in dictionary:
        return dictionary, len(w), dictionary[w]
        
    while w not in dictionary:
        removal = w_stack.pop()
        w = ''.join(w_stack)
    
    dictionary[msg[:len(w)+1]] = len(dictionary) + 1
    
    return dictionary, len(w), dictionary[w]

def solution(msg):
    dictionary = {ascii_uppercase[i]: i+1 for i in range(len(ascii_uppercase))}
    result = []
    
    while len(msg) > 0:
        dictionary, w_length, output = update_dictionary(dictionary, msg)
        msg = msg[w_length:]
        result.append(output)
        
    return result