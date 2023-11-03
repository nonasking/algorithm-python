# 햄버거 만들기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/133502#


def solution(ingredient):
    l = []
    
    for value in ingredient:
        l.append(value)
        while l[-4:] == [1,2,3,1]:
            del l[-4:]
                        
    return (len(ingredient) - len(l))//4