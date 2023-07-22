n = int(input())
v1, v2 = map(int, input().split())
m = int(input())
visited = [False] * (n + 1)
g = []
for i in range(n + 1):
    g.append([])
for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)


def dfs(g, v, v2, visited, cnt, flag):
    visited[v] = True
    for i in g[v]:
        if i == v2:
            print(cnt + 1)
            flag = True
            return flag
        if visited[i] is False:
            flag = dfs(g, i, v2, visited, cnt + 1, flag)

    return flag


if dfs(g, v1, v2, visited, 0, False) is False:
    print(-1)