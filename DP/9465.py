T = int(input())
for t in range(T):
    n = int(input())
    arr = []
    d = [[0]*(n+1) for i in range(2)]
    for i in range(2):
        arr.append(list(map(int, input().split())))
    d[0][1], d[1][1] = arr[0][0], arr[1][0]  # 점화식에 i-2가 들어가므로 0으로 이루어진 차원 추가
    for i in range(2, n+1):  # 점화식: d[][i] = max(d[][i-1], d[][i-2]) + arr[][i]
        d[0][i] = max(d[1][i-1], d[1][i-2]) + arr[0][i-1]  # 한 칸 잎 대각선과 두 칸 앞 대각선과의 max 비교
        d[1][i] = max(d[0][i-1], d[0][i-2]) + arr[1][i-1]
    print(max(d[0][n], d[1][n]))