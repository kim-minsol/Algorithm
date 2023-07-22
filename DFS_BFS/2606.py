n = int(input())
m = int(input())
g = []
for i in range(n+1):
    g.append([])
for i in range(m):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)
visited = [False] * (n+1)


def dfs(g, v, visited, cnt):
    visited[v] = True
    cnt += 1
    for i in g[v]:
        if not visited[i]:
            cnt = dfs(g, i, visited, cnt)
            visited[i] = True

    return cnt


print(dfs(g, 1, visited, -1))  # 시작 컴퓨터(1)은 카운트에서 제외