# 가운데 글자 가져오기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    m, r = divmod(len(s),2)
    if r == 1:
        return s[m]
    else:
        return s[m-1:m+1]