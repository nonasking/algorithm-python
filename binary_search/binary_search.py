
# 1. 기본 코드
# 재귀 함수로 구현
def binary_search_with_recursion(array, target, start, end):
	if start > end:
    	return None
    mid = (start + end) // 2
    if array[mid] == target:
    	return mid
    elif array[mid] > target:
    	return binary_search(array, target, start, mid-1)
    else:
    	return binary_search(array, target, mid+1, end)

# 반복문으로 구현
def binary_search_with_loop(array, target, start, end):
	while start <= end:
    	mid = (start + end) // 2
        if array[mid] == target:
        	return mid
        elif array[mid] > target:
        	end = mid-1
       	else:
        	start = mid+1
    return None

# 함수 호출 예
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_with_recursion(array, target, 0, n-1)
result = binary_search_with_loop(array, target, 0, n-1)
if result == None:
	print('원소가 존재하지 않습니다.')
else:
	print(result + 1)


# 2. bisect 라이브러리 사용
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))   # 2
print(bisect_right(a,x))  # 4

# 값이 특정 범위(left~right)에 속하는 데이터 갯수 구하기
def count_by_range(array, left_value, right_value):
	right_index = bisect_right(array, right_value)
	left_index = bisect_left(array, left_value)
	return right_index - left_index