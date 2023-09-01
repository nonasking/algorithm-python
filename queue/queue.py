# deque 라이브러리를 사용하여 구현
from collections import deque
queue = deque()
queue.append(5) # 값 추가
queue.popleft() # 먼저 들어간 값 제거
queue.pop()     # 나중에 들어간 값 제거 
...

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 큐 안의 값들 순서 뒤집기
print(queue) # 나중에 들어온 값부터 출력

# 리스트를 큐로 만들기
from collections import deque
l = [1,2,3]
queue = deque(l)