
# 값 1개 받기
# 기본
x = input()
# 형변환
x = int(input())
# 빠르게
import sys
x = sys.stdin.readline().rstrip()

# 값 여러개 받기
x, y = input().split()
# 형변환
x, y = map(int, input().split())
# 빠르게
x, y = sys.stdin.readline().split()
# 한줄씩
for x in sys.stdin:
  print(x.rstrip())

# 2차원 배열 받기
# 2처원 배열 담기
import sys

arr = list(map(int, sys.stdin.readline().split()))
grid = []
index = 0
n, m = 3, 4  # 행/열 갯수(예시)
for i in range(n):
  grid.append(arr[index:index + m])
  index += m

print(grid)