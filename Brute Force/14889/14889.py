from itertools import combinations

n = int(input())
arr = []
visited = [[False] * n for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))

c = list(combinations(range(n), n//2))

len_ = len(c)
min_ = 10000

for i in range(len_//2):
    sum1, sum2 = 0, 0
    c2 = list(combinations(c[i], 2))
    for comb in c2:
        sum1 += arr[comb[0]][comb[1]]
        sum1 += arr[comb[1]][comb[0]]
    c2 = list(combinations(c[len_-i-1], 2))
    for comb in c2:
        sum2 += arr[comb[0]][comb[1]]
        sum2 += arr[comb[1]][comb[0]]
    if min_ > abs(sum1 - sum2):
        min_ = abs(sum1 - sum2)

print(min_)