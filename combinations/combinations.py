# 조합
# 경우의 수는 nCr = n! / r! * (n-r)!
import math
print(math.comb(3,2))

# 각각의 경우를 직접 구할 경우
import itertools
data = [1,2,3]
for x in itertools.combinations(data,2):
	print(list(x), end=' ') # [1,2] [1,3] [2,3]

# 중복조합
import itertools
data = [1,2,3]
for x in itertools.combinations_with_replacement(data,2):
	print(list(x), end=' ') # [1, 1] [1, 2] [1, 3] [2, 2] [2, 3] [3, 3]
