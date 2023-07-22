from collections import deque

n, m = map(int, input().split())
map_ = []

for i in range(n):
    map_.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(map_):
    x, y = 0, 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        # if x == n-1 and y == m-1:
        #     break
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if map_[nx][ny] == 1:
                q.append((nx, ny))
                map_[nx][ny] = map_[x][y] + 1

bfs(map_)


print(map_[n-1][m-1])