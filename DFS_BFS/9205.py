from collections import deque

t = int(input())

def bfs(coord, visited, len_):
    q = deque([(coord[0][0], coord[0][1], 0)]) # deque 에 좌표 값 넣을 때 조심하기
    while q:
        x, y, idx = q.popleft()
        if x == coord[len_ - 1][0] and y == coord[len_ - 1][1]:
            print("happy")
            return True
        visited[idx] = True
        for i in range(len_):
            nx = coord[i][0]
            ny = coord[i][1]
            if abs(nx - x) + abs(ny - y) <= 1000:
                if visited[i] is False:
                    q.append((nx, ny, i))
    return False


for test in range(t):
    n = int(input())
    coord = []
    coord.append(list(map(int, input().split())))
    for i in range(n):
        coord.append(list(map(int, input().split())))
    coord.append(list(map(int, input().split())))
    visited = [False] * (n + 2)

    if bfs(coord, visited, n + 2) is False:
        print("sad")