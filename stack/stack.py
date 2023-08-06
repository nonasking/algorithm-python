# 리스트를 통해 스택 구현
stack = []
stack.append(5)
stack.append(2)
#...
stack.pop() # 가장 나중에 들어간 원소(맨 뒤의 원소) 제거
stack.append(1)
stack.pop()
#...
print(stack[::-1] # 최상단(나중에 들어간 순) 원소부터 출력
print(stack) # 최하단(먼저 들어간 순) 원소부터 출력