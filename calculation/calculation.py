# 나누기
print(8//2, 8%2)
print(divmod(8,2))

# 제곱근
import math
print(math.sqrt(2)) # 1.4142....

# 절댓값
print(abs(-1)) # 1

# 소수점 반올림
print(round(0.6)) # 1
# 원래 수와 올림/버림했을 때의 차이가 같은 경우 짝수 값 반환
print(round(0.5)) # 0
print(round(1.5)) # 2

# 소수점 올림
# 해당 값에서 + 방향으로 가장 가까운 정수 반환
import math
print(math.ceil(0.5)) # 1

# 소수점 버림
# 해당 값에서 0에 가까운 정수 반환
import math
print(math.trunc(-1.5)) # -1

# 소수점 내림
# 해당 값에서 - 방향으로 가장 가까운 정수 반환
import math
print(math.floor(-1.5)) # -2

# 소수의 개수
def get_divisors_count(n):
  answer = 0
  s = int(math.sqrt(n))
  for i in range(1,s+1):
    if n % i == 0:
      answer += 1
  if n == s**2 :
    return answer * 2 - 1
  return answer * 2