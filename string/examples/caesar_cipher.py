# 시저 암호(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def convert_alphabet(alphabet, n):
    upper_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    if alphabet == ' ':
        return ' '
    
    if alphabet.isupper():
        index = upper_alphabets.find(alphabet)+n
        if index >= len(upper_alphabets):
             index -= len(upper_alphabets)
        return upper_alphabets[index]
    else:
        index = lower_alphabets.find(alphabet)+n
        if index >= len(lower_alphabets):
             index -= len(lower_alphabets)
        return lower_alphabets[index]
        
    

def solution(s, n):
    result = [convert_alphabet(alphabet, n) for alphabet in s]
    answer = ''.join(result)
    
    return answer