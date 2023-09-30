h, w = map(int, input().split())
block = list(map(int, input().split()))

g = [[0]*w for i in range(h)]

for j in range(w):
    for i in range(h-1, -1, -1):
        if block[j] != 0:
            block[j] -= 1
            g[i][j] = 1

total = 0
for i in range(h):
    rain = 0
    point = 0
    for j in range(w):
        if g[i][j] == 1 and point == 0:
            point = 1
        elif point == 1 and g[i][j] == 0:
            rain += 1
        elif point == 1 and g[i][j] == 1 and rain > 0:
            total += rain
            rain = 0

print(total)