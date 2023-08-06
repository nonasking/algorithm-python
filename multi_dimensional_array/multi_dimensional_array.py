# n * n 배열 원소 출력
for i in range(n):
    for j in range(n):
        print(i,j)


# n * n 배열에서 동서남북으로 한 칸씩 이동(벡터값 선언)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

x, y = 1, 1 # 현재 위치 설정(예시)

for i in range(n):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(x,y)
