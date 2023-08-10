# x가 소수인지 아닌지 판별하는 함수(x는 2 이상의 자연수)
import math
def is_prime_number(x):
	# 2~x의 제곱근까지의 수 중에 x의 약수가 있는지 확인
	for i in range(2, int(math.sqrt(x))+1):
    	if x % i == 0:
        	return False
    return True


# 2~1000 사이의 모든 소수 판별 예시
import math
n = 1000 # 범위
array = [True for i in range(n+1)] # 소수인지 여부가 담긴 리스트(처음에는 0,1 제외하고는 모두 소수인 것으로 초기화)

# 에라토스테네스의 체 알고리즘 수행
# 2 ~ n의 제곱근까지 반복
for i in range(2, int(math.sqrt(n))+1):
	if array[i] == True:
    	# i를 제외한 i의 모든 배수들 지우기
        j = 2
        while i * j <= n:
        	array[i*j] = False
            j += 1

# 결과(2~n 안의 모든 소수) 출력
for i in range(2, n+1):
	if array[i]:
    	print(i, end=' ')