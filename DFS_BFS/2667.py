n = int(input())
g = []
for i in range(n):
    g.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
house = []


def dfs(g, x, y, cnt_h):
    cnt_h += 1
    g[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if g[nx][ny] == 1:
            cnt_h = dfs(g, nx, ny, cnt_h)

    return cnt_h


for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            house.append(dfs(g, i, j, 0))
            cnt += 1

print(cnt)
house.sort()
for i in range(cnt):
    print(house[i])
