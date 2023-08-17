n = int(input())
places = list(map(int, input().split()))

sum_ = [places[0]]
for i in range(1, n):
    sum_.append(sum_[i-1] + places[i])

#sum_ = [sum(places[:i+1]) for i in range(n)]

## 벌1: 맨 왼쪽, 벌2: 가운데 / 꿀통: 맨 오른쪽
sum1 = 0
for i in range(1, n - 1):
    sum1 = max(sum1, sum_[n-1] - places[0] - places[i] + sum_[n-1] - sum_[i])  # sum_[n-1]*2로 구할 경우 시간 초과(55점)

    ## 벌1 : 맨 왼쪽, 벌2 i번째에 존재
    ## 벌1의 꿀 양: 전체 합 - p[0] - p[i]
    ## 벌2의 꿀 양: 전체 합 - sum(i번째까지)
# print(sum1)


## 벌1: 맨 오른쪽, 벌2: 가운데 / 꿀통: 맨 왼쪽
sum2 = 0
for i in range(1, n - 1):
    sum2 = max(sum2, sum_[n-1] - places[n-1] - places[i] + sum_[i-1])

    ## 벌1 : 맨 오른쪽, 벌2 i번째에 존재
    ## 벌1의 꿀 양: 전체 합 - p[n-1] - p[i]
    ## 벌2의 꿀 양: 전체 합 - sum(i번째부터) = sum(i-1번째까지)

# print(sum2)


## 벌1, 벌2: 양 쪽 끝 / 꿀통 가운데
sum3 = 0
for i in range(1, n - 1):
    sum3 = max(sum3, sum_[i] - places[0] + sum_[n-1] - sum_[i-1] - places[n-1])
    ## 벌1 : 맨 오른쪽, 벌2 i번째에 존재
    ## 벌1의 꿀 양: sum_[i-1] - 벌1
    ## 벌2의 꿀 양: 전체 합 - sum_[i] - 벌2
# print(sum3)

print(max(sum1, sum2, sum3))