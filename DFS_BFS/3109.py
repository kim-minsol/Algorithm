r, c = map(int, input().split())
g = []
visited = []
for i in range(r):
    g.append(list(map(str, input())))
    visited.append([False] * c)

dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(g, visited, x, y, r, c):
    global cnt
    visited[x][y] = True
    if y == c - 1:  # 마지막 열에 도달했을 때
        cnt += 1
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or g[nx][ny]=='x' or visited[nx][ny] is True:
            continue
        if dfs(g, visited, nx, ny, r, c):
            return True  # if절로 return을 해주지 않으면 마지막 열에서도 계속해서 방문하게 됨.


cnt = 0
for i in range(r):
    dfs(g, visited, i, 0, r, c)

print(cnt)
