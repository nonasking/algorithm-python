# 최소 힙 구현
import heapq

# 오름차순 힙 정렬(Heap sort)
def heapsort(iterable):
	h = []
    result = []
    for value in iterable:
    	heapq.heappush(h, value)
    for i in range(len(h)):
    	result.append(heapq.heappop(h))
   	return result

result = heapsort([1,3,5,7,9,2,4,6,8,0]) # 0 1 2 3 4 5 6 7 8 9
print(result) 


# 최대 힙 구현
import heapq

# 내림차순 힙 정렬(Heap sort)
def heapsort(iterable):
	h = []
    result = []
    for value in iterable:
    	heapq.heappush(h, -value)
    for i in range(len(h)):
    	result.append(-heapq.heappop(h))
   	return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)  # 9 8 7 6 5 4 3 2 1 0

# 힙 메서드
# 리스트를 최소 힙으로 만들기
import heapq
l = [2,1,3]
heapq.heapify(l)
print(l) # [1, 2, 3]

# 힙에 원소 추가
import heapq
heap = [2]
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print(heap) # [1, 2, 3]

# 최소 힙에서 최솟값(첫 번째 값) 제거하면서 제거한 값 반환
import heapq
heap = [1,2,3]
heapq.heapify(heap)
min_value = heapq.heappop(heap)
print(min_value) # 1

