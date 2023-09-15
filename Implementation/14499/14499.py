n, m, x, y, k = map(int, input().split())
g = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [[0]*3 for i in range(4)]

def east():
    tmp = dice[1][2]
    for i in range(1, -1, -1):
        dice[1][i+1] = dice[1][i]
    dice[1][0] = dice[3][1]
    dice[3][1] = tmp

def west():
    tmp = dice[1][0]
    for i in range(2):
        dice[1][i] = dice[1][i+1]
    dice[1][2] = dice[3][1]
    dice[3][1] = tmp

def north():
    tmp = dice[0][1]
    for i in range(3):
        dice[i][1] = dice[i+1][1]
    dice[3][1] = tmp
    
def south():
    tmp = dice[3][1]
    for i in range(2, -1, -1):
        dice[i+1][1] = dice[i][1]
    dice[0][1] = tmp
    
    
    
for i in range(n):
    g.append(list(map(int, input().split())))


commend = list(map(int, input().split()))
for com in commend:
    nx = x + dx[com-1]
    ny = y + dy[com-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    if com == 1:
        east()
        
    elif com == 2:
        west()
        
    elif com == 3:
        north()
        
    elif com == 4:
        south()
    
    if g[nx][ny] == 0:
        g[nx][ny] = dice[3][1]
    else:
        dice[3][1] = g[nx][ny]
        g[nx][ny] = 0
    print(dice[1][1])
    #print("DICE", dice)
    x, y = nx, ny