# 딕셔너리 컴프리헨션
d = {index:'value' for index in range(10)} # {0: 'value', 1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value', 8: 'value', 9: 'value'}

# 키-값 삭제
d = {'k1':'v1','k2':'v2'} 
del d['k1']
print(d) # {'k2': 'v2'}

# 키 순서대로 정렬한 (키, 값) 리스트 반환
d = {2:'a',1:'b',3:'c'}
print(sorted(d.items())) # [(1, 'b'), (2, 'a'), (3, 'c')]