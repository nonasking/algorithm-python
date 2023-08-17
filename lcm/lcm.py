# a와 b의 최소공배수(LCM, Least Common Multiple)
def solution(a, b):
    max_num = a if a > b else b
    for i in range(max_num, a * b + 1):
        if i % a == 0 and i % b == 0:
            answer = i
            break
    return print(answer)