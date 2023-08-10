# 경우의 수는 nCr = n! / r! * (n-r)!
# 각각의 경우를 직접 구할 경우
import itertools
data = [1,2,3]
for x in itertools.combinations(data,2):
	print(list(x), end=' ') # [1,2] [1,3] [2,3]