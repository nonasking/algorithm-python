# 재귀 함수 기본 예시
from collections import deque
queue = deque()
queue.append(5) # 값 추가
queue.popleft() # 먼저 들어간 값 제거
...

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 큐 안의 값들 순서 뒤집기
print(queue) # 나중에 들어온 값부터 출력

# 팩토리얼 구현 예시
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)