n = int(input())

calender = []
arr = []
min_ = 100000
max_ = -1
for i in range(n):
    s, e = map(int, input().split())
    calender.append([s, e])
    if e > max_:
        max_ = e

arr = [0] * (max_ + 1)
calender.sort(key=lambda x: (x[0], -x[1]))


for i in range(n):
    s, e = calender[i]
    for i in range(s, e+1):
        arr[i] += 1


cnt = 0
ans = 0
range_ = 0
for k in arr:
    if k == 0:
        ans += (cnt * range_)
        cnt = 0
        range_ = 0
    else:
        if cnt < k:
            cnt = k
        range_ += 1
ans += (cnt * range_)
print(ans)
