from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

# 0: 북, 1: 동, 2: 남, 3: 서

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


cnt = 1
g[x][y] = -1
while True:
    flag = 0

    for i in range(4):
        d -= 1
        if d == -1:
            d = 3
        nx = x + dx[d]
        ny = y + dy[d]
        if g[nx][ny] == 0:  # map을 벗어날 일이 없음.
            x, y = nx, ny
            g[x][y] = -1  # 청소
            cnt += 1 # 청소한 칸의 개수
            flag = 1
            break

    if flag == 0:
        nx = x - dx[d]
        ny = y - dy[d]
        if g[nx][ny] == 1:
            break
        else:
            x, y = nx, ny


print(cnt)