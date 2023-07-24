from collections import deque

q = deque()
m, n, h = map(int, input().split())
max_ = 0
g = []
for i in range(h):
    gg = []
    for j in range(n):
        gg.append(list(map(int, input().split())))
        for k in range(m):
            if gg[j][k] == 1:
                q.append((i, j, k))
    g.append(gg)


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx >= h or nx < 0 or ny >= n or ny < 0 or nz >= m or nz < 0:
                continue
            if g[nx][ny][nz] == 0:
                g[nx][ny][nz] = g[x][y][z] + 1
                q.append((nx, ny, nz))


bfs()


for g1 in g:
    for g2 in g1:
        for g3 in g2:
            if g3 == 0:
                print(-1)
                exit(0)
        max_ = max(max_, max(g2))

print(max_ - 1)