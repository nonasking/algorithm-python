# 피보나치 수열 풀이법

# 1. 탑다운(재귀함수)
# DP 테이블의 길이 설정은 구할 값에 맞게 설정
d = [0] * 100

def fibo(x):
	if x ==1 or x == 2:
    	return 1
    if d[x] != 0:
    	return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99)) # 수열의 99번째 값(a99) 구하기

# 2. 보텀업(반복문)
# DP 테이블의 길이 설정은 구할 값에 맞게 설정
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
	d[i] = d[i-1] + d[i-2]

print(d[n])