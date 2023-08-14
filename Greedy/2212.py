n = int(input())
k = int(input())

sensors = list(map(int, input().split()))
diff = []

sensors.sort()

for i in range(1, n):
    diff.append(sensors[i] - sensors[i - 1])

diff.sort()

sum_ = 0
for i in range(n - k):
    sum_ += diff[i]

print(sum_)