n = int(input())
period = list(map(int, input().split()))
plan = list(map(int, input().split()))

arr = []
for k1, k2 in zip(period, plan):
    arr.append([k1, k2])  # 리스트 대응정렬을 위해서 두 개의 리스트를 우선적으로 묶음


arr.sort(key=lambda x: (x[1], x[0]))  # key 주입을 통해서 리스트 대응 정렬
# 계획을 기준으로 오름차순으로 정렬하되, 계획일이 같은 경우에는 기간을 기준으로 정렬


prev = arr[0][1]  # prev에 기프티콘 사용일 저장 
max_ = 0
ans = 0

for i in range(n):
    if prev > arr[i][0]:  # 기한 연장
        prev = max(prev, arr[i][1])
        cnt = (prev - arr[i][0] - 1) // 30 + 1  #  30 * cnt + p1 - p2 > 0
        arr[i][0] += cnt * 30
        ans += cnt
    
    max_ = max(max_, arr[i][0])  # 해당 사용일에서 가장 사용 예정일의 값이 클 때 이를 해당 변수에 저장
    
    if i + 1 < n and arr[i + 1][1] != arr[i][1]:  # 계획일이 달라질 경우, 해당 구간에서 마지막으로 기프티콘을 사용한 날짜를 prev에 저장 
        prev = max_

    
print(ans)