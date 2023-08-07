# 배열 안의 수 중 연속되는 가장 긴 수열 구하기
arr = [1,2,6,4,5,2]
n = len(arr)

arr.reverse()

dp = [1] * n

for i in range(1,n):
  for j in range(0,i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[i], dp[i]+1)

print(max(dp))