# N개의 최소공배수(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/12953


def get_lcm(num1, num2):
    bigger = num1 if num1 > num2 else num2
    for num in range(bigger, num1*num2+1):
        if num % num1 == 0 and num % num2 == 0:
            return num
    return num1 * num2


def solution(arr):
    lcm = arr[0]
    i = 1
    while True:
        lcm = get_lcm(lcm, arr[i])
        i += 1
        if i == len(arr):
            break
    return lcm