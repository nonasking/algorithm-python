# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, x):
	# 부모 노드가 아니라면, 부모 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
    	parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
    if a < b:
    	parent[b] = a
    else:
    	parent[a] = b

# 노드의 개수, 간선의 개수 입력받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v+1) 

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
	parent[i] = i

# 사이클 발생 여부
is_cycle = False

for i in range(e):
	a, b = map(int,input().split())
    # 사이클이 발생 -> 반복문 중지(종료)
    if find_parent(parent, a) == find_parent(parent, b):
    	is_cycle = True
        break
    # 사이클이 발생하지 않음 -> 합집합 연산 수행
    else:
    	union_parent(parent, a, b)

# 사이클 발생 여부 출력
if is_cycle:
	print('사이클 발생 O')
else:
	print('사이클 발생 X')