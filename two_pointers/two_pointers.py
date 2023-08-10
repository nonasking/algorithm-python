# 특정 합 m을 가지는 부분 연속 수열의 개수 구하기
n = 5 # 데이터의 개수
m = 5 # 찾고자 하는 부분합 m
data = [1,2,3,4,5] # 전체 수열

count = 0 # 부분합의 개수
interval_sum = 0 # m과 비교할 부분합
end = 0 # 끝점

# 시작점(start)을 차례대로 증가시키며 반복
for start in range(n):
	# 끝점(end)을 가능한 오른쪽으로 이동
    while interval_sum < m and end < n:
    	interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 + 1
    if interval_sum == m:
    	count += 1
    interval_sum -= data[start]

# 결과(부분합의 개수) 출력
print(count)