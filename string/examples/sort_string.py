# 문자열 내림차순으로 배치하기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    big = []
    small = []
    
    for letter in s:
        if letter.isupper():
            big.append(letter)
        else:
            small.append(letter)
    
    answer = ''.join(sorted(small, reverse=True) + sorted(big, reverse=True))
    
    return answer
