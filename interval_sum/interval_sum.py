# n개의 정수로 구성된 수열에서, m개의 쿼리에 대해 각 쿼리 구간에 포함된 데이터의 합을 구하기
# 데이터의 개수 n과 데이터
n = 5
data = [1,2,3,4,5]

# 접두사 합 배열 prefix_sum 구하기
sum_value = 0
prefix_sum = [0]
for i in data:
	sum_value += i
    prefix_sum.append(sum_value)

# 세 번째부터 네 번째까지의 구간 합 계산
left, right = 3, 4
print(prefix_sum[right] - prefix_sum[left-1])