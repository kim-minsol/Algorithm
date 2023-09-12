import sys

n, m = map(int, input().split())
s = [sys.stdin.readline().strip() for i in range(n)]

cnt = 0
for i in range(m):
    k = sys.stdin.readline().strip()
    if k in s:
        cnt += 1

print(cnt)