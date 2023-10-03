from collections import deque

n, k = map(int, input().split())
t = 0
q = deque([(n, t)])
visited = [False] * 100001

dx = [-1, 1]
visited[n] = True


def bfs(q, dx, n, k):
    while q:
        x, t = q.popleft()
        if x == k:
            print(t)
            exit()
        nx = x * 2
        if nx <= 100000 and visited[nx] is False:
            q.append((x*2, t))
            visited[x*2] = True
        for i in range(2):
            nx = x + dx[i]
            if nx < 0 or nx > 100000:
                continue
            if visited[nx] is False:
                q.append((nx, t+1))
                visited[nx] = True


bfs(q, dx, n, k)