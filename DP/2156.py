n = int(input())
arr = [0]
dp = [0] * (n+1)
for i in range(n):
    arr.append(int(input()))

dp[1] = arr[0]
dp[2] = arr[0] + arr[1]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]))
    
print(dp[n])
