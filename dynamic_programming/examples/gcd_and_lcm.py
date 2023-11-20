# 최대공약수와 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12940


def get_gcd(n, m):
    if n % m == 0:
        return m
    else:
        return get_gcd(m, n % m)

def solution(n, m):
    numbers = sorted([n,m], reverse=True)
    gcd = get_gcd(numbers[0], numbers[1])
    lcm = n * m // gcd
    return [gcd, lcm]