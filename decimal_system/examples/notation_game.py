# n진수 게임(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/17687


def convert_number(n, num):
    strs = '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'
    result = ''
    while num != 0:
        num, remain = divmod(num,n)
        result += str(strs[remain])
    return result[::-1]
    
def get_answers(n, t, m, p):
    num = 0
    answers = '0'
    while True:
        answers += convert_number(n, num)
        if len(answers) >= m*t:
            break
        num += 1
    return answers
    
def solution(n, t, m, p):
    answers = get_answers(n, t, m, p)
    
    result = ''
    for i in range(1,len(answers)+1):
        if m > p and i % m == p and len(result) < t:
            result += answers[i-1]
        elif m == p and i % m == 0 and len(result) < t:
            result += answers[i-1]
    
    return result