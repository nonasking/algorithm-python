
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
x, y = map(int,sys.stdin.readline().split())