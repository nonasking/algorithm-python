# 최솟값 만들기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12941


def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)
    
    multiples = []
    for i in range(len(A)):
        multiples.append(A[i] * B[i])
    
    return sum(multiples)