# 10진법 -> N진법 변환
import sys

n, b = map(int, sys.stdin.readline().split())

s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ''
while n != 0:
  n, r = divmod(n,b)
  result += str(s[r])

print(result[::-1])