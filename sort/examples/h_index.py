# H-Index(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42747


def get_count(citations, h):
    return len([i for i in citations if i >= h])

def solution(citations):

    citations.sort(reverse=True)
    i = citations[0]
    
    while True:
        if get_count(citations, i) >= i:
            return i
        else:
            i -= 1
        if i == 0:
            return -1