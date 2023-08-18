# 리스트 메서드 정리

# 리스트의 특정 인덱스에 값 삽입
l = ['a','b','c','d']
l.insert(1,'z')
print(l) # ['a','z','b','c','d']

# 리스트의 특정 인덱스 값 삭제
l = ['a','b','c','d']
del(l[1])
print(l) # ['a','c','d']

# 리스트 끝에 요소 삽입
l = ['a','b','c','d']
l.append('z')
print(l) # ['a','b','c','d','z']

# 값으로 인덱스 찾기
l = ['a','b','c','a']
print(l.index('a')) # 0

# 리스트 값 모두 삭제(비우기)
l = ['a','b','c','d']
l.clear()
print(l)

# 리스트의 특정 요소 삭제
l = ['a','b','c','d']
l.remove('b')
print(l) # ['a','c','d']

# 리스트에서 특정 요소가 등장하는 첫 번째 인덱스 반환
l = ['a','b','c','d','b']
print(l.index('b')) # 1
print(l.index('z')) # ValueError