# x가 소수인지 아닌지 판별하는 함수(x는 2 이상의 자연수)
import math
def is_prime_number(x):
	# 2~x의 제곱근까지의 수 중에 x의 약수가 있는지 확인
	for i in range(2, int(math.sqrt(x))+1):
    	if x % i == 0:
        	return False
    return True