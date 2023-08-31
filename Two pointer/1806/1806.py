n, s = map(int, input().split())
arr = list(map(int, input().split()))
## 변수 초기화
len_ = 0  # 구간 길이
end = 0  # end idx
interval_sum = 0  # 부분합

for start in range(n):  # start idx는 순차적으로 증가
    while end < n and interval_sum < s:  # end idx는 부분합 조건을 충족시킬 때까지 증가
        interval_sum += arr[end]
        end += 1

    if interval_sum >= s:
        if len_ == 0:  # 부분합 조건 만족하는 경우 (0이 아니게 됨)
            len_ = end - start
        elif len_ > end - start:  # 최소 길이 갱신
            len_ = end - start

    interval_sum -= arr[start]  # start idx는 순차적으로 증가하므로, 이를 부분합에 반영


print(len_)