# 10진법 -> N진법 변환
import sys

n, b = map(int, sys.stdin.readline().split())

s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ''
while n != 0:
  n, r = divmod(n,b)
  result += str(s[r])

print(result[::-1])

# N진법 -> 10진법 변환
import sys

n, b = sys.stdin.readline().split()
b = int(b)

result = 0
for i in range(len(n)):
  if n[-i-1].isalpha():
    result += b ** i * (ord(n[-i-1])-55)
  else:
    result += b ** i * int(n[-i-1])

print(result)