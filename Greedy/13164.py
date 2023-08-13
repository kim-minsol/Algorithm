n, k = map(int, input().split())
h = list(map(int, input().split()))
diff = []

for i in range(1, n):
    diff.append(h[i] - h[i - 1])  # 인접한 원생의 키 차이를 새로운 배열에 저장.

diff.sort()  # 키 차이 배열 정렬 -> 키 차이가 작은 값이 오름차순으로 정렬

sum_ = 0
for i in range(n - k):  # k-1개의 큰 키 차이를 제외하고 합을 구해야 함.
    sum_ += diff[i]  # n - (k - 1) - 1 -> n - k


print(sum_)