# 짝지어 제거하기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12973


def solution(s):
    stack = []
    alphabets = []
    i = 0
    while True:
        if len(stack) > 0:
            if stack[-1] == s[i]:
                removal = stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
        i += 1
        if i == len(s):
            return 1 if len(stack) == 0 else 0