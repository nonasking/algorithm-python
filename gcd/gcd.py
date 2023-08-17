# 최대공약수(GCD, Greatest Common Divisor) 구하기
# a>b라고 가정
def gcd(a,b):
	if a % b == 0:
    	return b
    else:
    	return gcd(b, a%b)

print(gcd(192,162)) # 6