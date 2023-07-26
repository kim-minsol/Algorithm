from collections import deque

n, m = map(int, input().split())
visited = [0] * 100001
q = deque([n])

dv = [-1, 1, 2]


def bfs(v, m, visited):
    while q:
        v = q.popleft()
        if v == m:
            return visited[v]
        else:
            for i in range(3):
                if i == 2:
                    nv = 2 * v
                else:
                    nv = v + dv[i]
                if nv < 0 or nv > 100000:
                    continue
                if visited[nv] == 0:
                    visited[nv] = visited[v] + 1
                    q.append(nv)


print(bfs(n, m, visited))