from collections import deque

n, l, r = map(int, input().split())
arr = []
visited = [[False]*n for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(map(int, input().split())))

def bfs(a, b):
    if visited[a][b] == True:
        return 0
    visited[a][b] = True
    q = deque([(a, b)]) # x, y 해치지 않기 위해 a, b 사용
    
    move = [[a, b]]  # 인구 이동 필요한 마을 저장
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] is True:
                continue

            if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                visited[nx][ny] = True
                q.append([nx, ny])
                move.append([nx, ny])
    
    sum_ = 0  # 조사한 마을들에서의 인구 수 계산 및 적용
    len_ = len(move)
    for x, y in move:
        sum_ += arr[x][y]
    k = sum_ // len_
    for x, y in move:
        arr[x][y] = k
    
    if len_ > 1:  # 두 개 이상의 마을에서 인구 이동 발생
        return 1
    else:
        return 0


def make_False(visited, n):  # 노드 방문 그래프 초기화 함수
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

ans = 0  # 인구 이동 날짜
while True:
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] is False:
                flag += bfs(i, j)
    if flag > 0:  # flag가 0보다 크다면 인구 이동이 일어난 경우임.
        ans += 1
        make_False(visited, n)  # 인구 이동 시 노드 방문 그래프를 초기화해야 함.
    else:
        break

print(ans)
