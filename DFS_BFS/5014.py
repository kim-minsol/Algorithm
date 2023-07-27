from collections import deque

f, s, g, u, d = map(int, input().split())

q = deque([s])
visited = [0] * (f + 1)
visited[s] = 1 # dv가 0이 되는 경우 고려 -> 출력 시 -1
dv = [u, -d]


def bfs(s, g, visited):
    while q:
        v = q.popleft()
        if v == g:
            return visited[v]
        for i in range(2):
            nv = v + dv[i]
            if nv < 1 or nv > f:
                continue
            if visited[nv] == 0:
                visited[nv] = visited[v] + 1
                q.append(nv)


k = bfs(s, g, visited)
if k == None:
    print("use the stairs")
else:
    print(k - 1)