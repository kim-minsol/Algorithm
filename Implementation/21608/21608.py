n = int(input())
students = [list(map(int, input().split())) for i in range(n ** 2)]
g = [[0]*n for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def seat(g, s):
    max_adj = -1
    max_blnk = -1
    seat_x, seat_y = -1, -1
    for x in range(n-1, -1, -1): # 3번 조건 만족 위해 거꾸로 탐색함.
        for y in range(n-1, -1, -1):
            cnt_adj = 0
            cnt_blnk = 0
            if g[x][y] == 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if g[nx][ny] in s[1:]:
                        cnt_adj += 1
                    if g[nx][ny] == 0:
                        cnt_blnk += 1
                if max_adj == cnt_adj:
                    if max_blnk <= cnt_blnk:
                        seat_x, seat_y = x, y
                        max_adj, max_blnk = cnt_adj, cnt_blnk
                elif max_adj < cnt_adj:
                    seat_x, seat_y = x, y
                    max_adj, max_blnk = cnt_adj, cnt_blnk
    return seat_x, seat_y


for i in range(n ** 2):
    s = students[i]
    x, y = seat(g, s)
    g[x][y] = s[0]



# 만족도 계산
comfort = 0
for s in students:
    for x in range(n):
        for y in range(n):
            if g[x][y] == s[0]:
                cnt = 0
                for t in range(4):
                    nx = x + dx[t]
                    ny = y + dy[t]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if g[nx][ny] in s[1:]:
                        cnt += 1
                if cnt == 1:
                    comfort += 1
                elif cnt == 2:
                    comfort += 10
                elif cnt == 3:
                    comfort += 100
                elif cnt == 4:
                    comfort += 1000

print(comfort)