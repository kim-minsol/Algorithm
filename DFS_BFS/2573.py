import sys

sys.setrecursionlimit(100000) # 재귀 함수 제한이 990개이므로, sys 활용하여 재귀 함수 제한 해제

n, m = map(int, input().split())
g = []

for i in range(n):
    g.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(g, x, y, visited):
    visited[x][y] = True
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if g[nx][ny] == 0 and g[x][y] - cnt > 0 and visited[nx][ny] is False:
            cnt += 1
        elif visited[nx][ny] is False and g[nx][ny] > 0: # 바다가 -가 될 수 있기 때문
            dfs(g, nx, ny, visited)
    g[x][y] -= cnt  # 인접한 바다의 개수만큼 빙산 녹이기


ans = 0
for year in range(10000): # year가 10을 넘을 수도 있음 !!
    chunk = 0
    visited = [[False for j in range(m)] for i in range(n)]
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0 and visited[x][y] is False:
                dfs(g, x, y, visited)
                chunk += 1

    if chunk > 1:
        ans = year
        break


print(ans)