# 문자열 내 마음대로 정렬하기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    sorted_strings = []
    for i,v in enumerate(strings):
        new_string = v[n] + v[:n] + v[n+1:]
        sorted_strings.append(new_string)
    sorted_strings.sort()
    answer = []
    for i,v in enumerate(sorted_strings):
        new_string = v[1:n+1] + v[0] + v[n+1:]
        answer.append(new_string)
    return answer