from collections import deque

n, l, r = map(int, input().split())
arr = []
visited = [[False]*n for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(map(int, input().split())))

def bfs(a, b):
    q = deque([(a, b)]) # x, y 해치지 않기 위해 a, b 사용
    cnt = 1
    k = arr[a][b]
    move = [[a, b]]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] is True:
                continue

            if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                q.append([nx, ny])
                visited[nx][ny] = True
                move.append([nx, ny])
                cnt += 1
                k += arr[nx][ny]
    
    print(k)
    print(move)
    k = k // cnt
    print(k ,cnt)
    for x, y in move:
        arr[x][y] = k
    
    if cnt > 1:
        return 1
    else:
        return 0


def make_zero(visited, n):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

ans = 0
while True:
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] is False:
                flag += bfs(i, j)
    if flag > 0:
        ans += 1
        print(arr)
        make_zero(visited, n)
    else:
        break

print(ans)
print(arr)


# 문제 해결 중...