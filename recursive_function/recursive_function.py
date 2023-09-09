# 재귀 함수 기본 예시

# 피보나치 수열 예시
def fibo(x):
	if x == 1 or x == 2:
    	return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4)) # 수열의 4번째 값(a4) 구하기

# 팩토리얼 구현 예시
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)