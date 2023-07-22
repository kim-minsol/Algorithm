from collections import deque

n, m, v = map(int, input().split())
# g = []*(n+1)
g = []
for i in range(n+1):
    g.append([])

for i in range(m):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

for i in range(n):
    g[i+1].sort()


def dfs(g, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(len(g[v])):
        if visited[g[v][i]] is False:
            dfs(g, g[v][i], visited)


def bfs(g, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        vertex = q.popleft()
        print(vertex, end=" ")
        for i in g[vertex]:
            if visited[i] is False:
                q.append(i)
                visited[i] = True


visited = [False]*(n+1)
dfs(g, v, visited)
print()

visited = [False]*(n+1)
bfs(g, v, visited)