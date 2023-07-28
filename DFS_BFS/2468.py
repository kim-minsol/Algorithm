import sys

sys.setrecursionlimit(100000) # 재귀 함수 제한이 990개이므로, sys 활용하여 재귀 함수 제한 해제

n = int(input())
g = []

for i in range(n):
    g.append(list(map(int, input().split())))

    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, rain):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or g[nx][ny] <= rain: # 그래프를 벗어나거나, 물에 잠긴 영역은 방문 x
            continue
        if visited[nx][ny] is False: # 방문하지 않은 노드인 경우
            dfs(nx, ny, rain)
    


max_h = 0
for arr in g:
    max_h = max(max(arr), max_h)

max_ = 0
for rain in range(max_h + 1):
    cnt = 0
    visited = [[False for i in range(n)] for j in range(n)] # 이때 list comprehension 사용 안 하면 메모리 초과 일어날 수 있음
    for x in range(n):
        for y in range(n):
            if rain < g[x][y] and visited[x][y] is False:
                dfs(x, y, rain)
                cnt += 1
    if cnt > max_:
        max_ = cnt
        

print(max_) # 해당 코드를 pypy3에 넣었을 때 메모리 초과가 일어나지만 python3에선 통과되었음.
# pypy3는 속도가 python에 비해 빠른 대신 메모리를 더 많이 사용하기 때문