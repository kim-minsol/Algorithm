n = int(input())
k = int(input())
g = [[0]*n for i in range(n)]
snake = [[0, 0]]

d_list = []
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    x, y = map(int, input().split())
    g[x-1][y-1] = 1  # 사과

l = int(input())
for i in range(l):
    x, c = input().split()
    x = int(x)
    d_list.append([x, c])

x, y = 0, 0
time = 0
flag = 0
while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 벽에 부딫혔을 때
        print(time)
        break
    for s in snake:
        if nx == s[0] and ny == s[1]:
            print(time)
            flag = 1
    if flag == 1:
        break
    snake.append([nx, ny])
    if g[nx][ny] == 0:
        snake.pop(0)  # 사과가 없을 경우에, 꼬리가 위치한 칸을 비워준다.
    elif g[nx][ny] == 1:
        g[nx][ny] = 0  # 사과를 먹으면 그 칸의 사과가 없어져야 함.
    for num, c in d_list:
        if num == time:
            if c == 'L':
                direction = (direction - 1 + 4) % 4
            elif c == 'D':
                direction = (direction + 1) % 4
            break
    x, y = nx, ny
