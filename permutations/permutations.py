# 순열
# 경우의 수는 nPr = n! / (n-r)!
# 각 경우를 직접 구할 경우
import itertools
data = [1,2]
for x in itertools.permutations(data,2):
	print(list(x), end=' ') # [1,2] [2,1]


# 중복순열
import itertools
data = [1,2]
for x in itertools.product(data,repeat=2):
	print(list(x), end=' ') # [1, 1] [1, 2] [2, 1] [2, 2]
