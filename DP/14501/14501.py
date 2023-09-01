n = int(input())
arr = [[0 ,0]]
dp = [[0]*2 for i in range(n + 1)]

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n+1):
    if arr[i][0] + i > n+1:
        continue
    for j in range(1, i):
        if dp[j][0] <= i and dp[i][1] < dp[j][1] + arr[i][1]:
            dp[i][1] = dp[j][1] + arr[i][1]
            dp[i][0] = i + arr[i][0]
    if dp[i][1] == 0 and arr[i][0] <= n:
        dp[i][1] = arr[i][1]
        dp[i][0] = arr[i][0] + i

print(max(dp, key = lambda x:x[1])[1])