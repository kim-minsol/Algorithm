n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()

prefix_sum = 0

left, right = 1, arr[n-1]
ans = 0

while left <= right:
    mid = (left + right) // 2
    sum_ = 0
    for i in range(n):
        if arr[i] <= mid:
            sum_ += arr[i]
        else:
            sum_ += mid
    if sum_ <= m:
        if ans < sum_:
            ans = mid
            left = mid + 1
    else:
        right = mid - 1

print(ans)